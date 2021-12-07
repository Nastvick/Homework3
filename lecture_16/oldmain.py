def daily(context: CallbackContext):
    message = "Hello, this message will be sent only once"
    with Session() as session:
        for user in session.query(User).filter(User.show_notifications == True):
            context.bot.send_message(chat_id=user.telegram_id, text=message)




j = updater.job_queue
j.run.once(once,10)

job_daily = j.run_daily(daily, days=tuple(rang(7)))