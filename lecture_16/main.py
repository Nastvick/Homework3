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

from models import User

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

class DescriptionWeakness(IntEnum):
    TITLE = auto()
    DESCRIPTION = auto()
    DATE = auto()
    CONFIRM = auto()




def start(update: Update, context: CallbackContext):
    telegram_id = update.effective_user.id
    update.message.reply_text('Enter your weakness:', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True,
    ))
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
    update.message.reply_text('Enter your weakness title:', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True,
    ))

    return DescriptionWeakness.TITLE


def get_task_title(update: Update, context: CallbackContext):
    context.user_data['title'] = update.message.text

    reply_keyboard = [['/skip', '/cancel']]

    update.message.reply_text('Enter your weakness description:', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True,
    ))

    return DescriptionWeakness.DESCRIPTION #input date

def get_task_description(update: Update, context: CallbackContext):
    if update.message.text == '/start':
        user = User(
            telegram_id=telegram_id,
            username=update.effective_user.username,
            first_name=update.effective_user.first_name,
            last_name=update.effective_user.last_name,
            weakness_start_date=update.effective_user.weakness_start_date,
            weakness_title=update.effective_user.weakness_title,
        )
        context.user_data['description'] = None
    else:
        context.user_data['description'] = update.message.text


    reply_keyboard = [['/skip', '/cancel']]
    update.message.reply_text('Enter start date!', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True,
    ))
        session.add(user)
        session.commit()
        update.message.reply_text(
        "You are doing great! Keep up!",

    return DescriptionWeakness.DATE #conversation end + create record db

def days(update: Update, context: CallbackContext):
    if update.message.text == '/days':

    return #number of days user is holding on


def failed(update: Update, context: CallbackContext):
    if update.message.text == '/failed':
        #date today automatically
        if update.message.text == '/skip':
            context.user_data['date'] = None
        else:
            context.user_data['date'] = datetime.datetime.strptime(update.message.text, "%d/%m/%Y")

        reply_keyboard = [['/skip', '/cancel']]
        update.message.reply_text('Enter place!', reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True,
        ))
        session.add(user)
        session.commit()
        update.message.reply_text(
            "Don't give up! You should start over!",



dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('failed', failed))
dispatcher.add_handler(CommandHandler('days', days))


if __name__ == '__main__':
    updater.start_polling()
    updater.idle()