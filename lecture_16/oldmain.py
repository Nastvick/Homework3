import datetime
import logging
import os

from enum import auto, IntEnum

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters, ConversationHandler, Updater, \
    CallbackQueryHandler

from models import User, Task


load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

updater = Updater(token=os.getenv("TOKEN"), use_context=True)
dispatcher = updater.dispatcher



engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Session = sessionmaker(engine)


class NewTaskStates(IntEnum):
    TITLE = auto()
    DESCRIPTION = auto()
    DATE = auto()
    PLACE = auto()
    CONFIRM = auto()


class ShowTasks(IntEnum):
    ALL = auto()
    TODAY = auto()
    TOMORROW = auto()
    COMPLETED = auto()
    NOT_COMPLETED = auto()

    def to_string(self):
        return f'show-tasks-{self.value}'


class TaskCompletion(IntEnum):
    COMPLETED = auto()
    NOT_COMPLETED = auto()


def start(update: Update, context: CallbackContext):
    telegram_id = update.effective_user.id
    with Session() as session:
        existing_user = session.query(User).get(telegram_id)
        if existing_user is None:
            user = User(
                telegram_id=telegram_id,
                username=update.effective_user.username,
                first_name=update.effective_user.first_name,
                last_name=update.effective_user.last_name,
            )
            session.add(user)
            session.commit()
            update.message.reply_text(
                "You are registered!",
            )
        else:
            update.message.reply_text(
                f"You are already registered, "
                f"{update.effective_user.username if update.effective_user.username is not None else 'Incognito'}! ",
            )


def new_task(update: Update, context: CallbackContext):
    reply_keyboard = [['/cancel']]
    update.message.reply_text('Enter your task title:', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True,
    ))

    return NewTaskStates.TITLE


def get_task_title(update: Update, context: CallbackContext):
    context.user_data['title'] = update.message.text

    reply_keyboard = [['/skip', '/cancel']]

    update.message.reply_text('Enter task description:', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True,
    ))

    return NewTaskStates.DESCRIPTION #input date


def get_task_description(update: Update, context: CallbackContext):
    if update.message.text == '/skip':
        context.user_data['description'] = None
    else:
        context.user_data['description'] = update.message.text

    reply_keyboard = [['/skip', '/cancel']]
    update.message.reply_text('Enter task date!', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True,
    ))

    return NewTaskStates.DATE #conversation end + create record db


def get_task_date(update: Update, context: CallbackContext):
    if update.message.text == '/skip':
        context.user_data['date'] = None
    else:
        context.user_data['date'] = datetime.datetime.strptime(update.message.text, "%d/%m/%Y")

    reply_keyboard = [['/skip', '/cancel']]
    update.message.reply_text('Enter place!', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True,
    ))

    return NewTaskStates.PLACE


def get_task_place(update: Update, context: CallbackContext):
    if update.message.text == '/skip':
        context.user_data['place'] = None
    else:
        context.user_data['place'] = update.message.text

    task = Task(
        title=context.user_data["title"],
        description=context.user_data["description"],
        when_date=context.user_data["date"],
        place=context.user_data["place"],
    )
    reply_keyboard = [['YES', 'NO']]
    update.message.reply_text(f'Here is your task!\n{task.display()}', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, input_field_placeholder='Create (Yes/No)?'
    ))

    return NewTaskStates.CONFIRM


def create_task(update: Update, context: CallbackContext):
    with Session() as session:
        user_new_task = Task(
            user_id=update.effective_user.id,
            title=context.user_data['title'],
            description=context.user_data['description'],
            when_date=context.user_data['date'],
            place=context.user_data['place'],
        )
        session.add(user_new_task)
        session.commit()
    update.message.reply_text('Hooray, your task is created!')

    return ConversationHandler.END


def cancel_creation_task(update: Update, context: CallbackContext):
    update.message.reply_text('See you...')

    return ConversationHandler.END


def get_tasks(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Select one of the buttons:',
        reply_markup=InlineKeyboardMarkup.from_column(
            [
                InlineKeyboardButton(text='All tasks', callback_data=ShowTasks.ALL.to_string()),
                InlineKeyboardButton(text='Today tasks', callback_data=ShowTasks.TODAY.to_string()),
                InlineKeyboardButton(text='Tomorrow tasks', callback_data=ShowTasks.TOMORROW.to_string()),
                InlineKeyboardButton(text='Completed tasks', callback_data=ShowTasks.COMPLETED.to_string()),
                InlineKeyboardButton(text='Not completed tasks', callback_data=ShowTasks.NOT_COMPLETED.to_string()),
            ]
        ),
    )


def show_tasks_callback(update: Update, context: CallbackContext, logger=None) -> None:
    update.callback_query.answer()
    with Session() as session:
        query = session.query(Task).filter_by(user_id=update.effective_user.id).order_by(Task.creation_date)
        if update.callback_query.data == ShowTasks.ALL.to_string():
            query = query.all()
        elif update.callback_query.data == ShowTasks.TODAY.to_string():
            query = query.filter(Task.when_date <= datetime.date.today()).filter(Task.is_completed == False)
        elif update.callback_query.data == ShowTasks.TOMORROW.to_string():
            query = query.filter(Task.when_date > datetime.date.today()).filter(Task.is_completed == False)
        elif update.callback_query.data == ShowTasks.COMPLETED.to_string():
            query = query.filter(Task.is_completed == True)
        elif update.callback_query.data == ShowTasks.NOT_COMPLETED.to_string():
            query = query.filter(Task.is_completed == False)
        else:
            logger.info("Not supported event")
            return

        tasks = list(query)
        if len(tasks):
            for task in tasks:
                update.effective_message.reply_markdown_v2(
                    task.display_markdown(),
                    reply_markup=InlineKeyboardMarkup.from_row(
                        [
                            InlineKeyboardButton(
                                text='✅️',
                                callback_data=f'mark-task${TaskCompletion.COMPLETED}${task.id}',
                            ),
                            InlineKeyboardButton(
                                text='❌️',
                                callback_data=f'mark-task${TaskCompletion.NOT_COMPLETED}${task.id}',
                            ),
                        ]
                    ),
                )
        else:
            update.effective_message.reply_text('There are no tasks!')


def mark_task_completion_callback(update: Update, context: CallbackContext, logger=None):
    update.callback_query.answer()
    with Session() as session:
        query = session.query(Task).filter_by(user_id=update.effective_user.id).order_by(Task.creation_date)
        _, completion, task_id = update.callback_query.data.split('$')

        logger.info("BEFORE")
        task = query.filter(Task.id == int(task_id)).first()
        logger.info("TASK %s", task)
        if task is None:
            logger.info("Not found task in user tasks")
            return

        completion = TaskCompletion(int(completion))
        if completion == TaskCompletion.COMPLETED:
            task.is_completed = True
        elif completion == TaskCompletion.NOT_COMPLETED:
            task.is_completed = False
        else:
            logger.info("Not valid completion value")
            return
        session.commit()
        update.effective_message.edit_text(
            task.display_markdown(),
            reply_markup=InlineKeyboardMarkup.from_row(
                [
                    InlineKeyboardButton(
                        text='✅️',
                        callback_data=f'mark-task${TaskCompletion.COMPLETED}${task.id}',
                    ),
                    InlineKeyboardButton(
                        text='❌️',
                        callback_data=f'mark-task${TaskCompletion.NOT_COMPLETED}${task.id}',
                    ),
                ]
            ),
            parse_mode=ParseMode.MARKDOWN_V2,
        )


new_task_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('new_task', new_task)],#start
    states={
        NewTaskStates.TITLE: [MessageHandler(Filters.text & ~Filters.command, get_task_title)],
        NewTaskStates.DESCRIPTION: [MessageHandler(Filters.text, get_task_description)],
        NewTaskStates.DATE: [
            MessageHandler(Filters.regex('^\d{2}\/\d{2}\/\d{4}$') | Filters.regex('^/skip$'), get_task_date),
        ],
        NewTaskStates.PLACE: [MessageHandler(Filters.text, get_task_place)],
        NewTaskStates.CONFIRM: [
            MessageHandler(Filters.regex('^(YES)$') & ~Filters.command, create_task),
            MessageHandler(Filters.regex('^(NO)$') & ~Filters.command, cancel_creation_task),
        ],
    },
    fallbacks=[
        CommandHandler('cancel', cancel_creation_task),
    ],
)
dispatcher.add_handler(new_task_conversation_handler)

show_tasks_converstion_handler = ConversationHandler(
    entry_points=[CommandHandler('tasks', get_tasks)],
    states={

    },
    fallbacks=[
        CommandHandler('cancel', cancel_creation_task),
    ],
)
dispatcher.add_handler(show_tasks_converstion_handler)
dispatcher.add_handler(CallbackQueryHandler(
    show_tasks_callback,
    pattern='^show-tasks',
))
dispatcher.add_handler(CallbackQueryHandler(
    mark_task_completion_callback,
    pattern='^mark-task',
))

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('failed', failed))
dispatcher.add_handler(CommandHandler('days', days))


#days command + def days
# def days


if __name__ == '__main__':
    updater.start_polling()
    updater.idle()