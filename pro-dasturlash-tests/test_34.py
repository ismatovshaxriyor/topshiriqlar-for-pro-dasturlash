from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton

ADMIN_ID = 2048383791

def show_menu(update, contetx):
    buttons = []

def start_cmd(update, context):
    print(update.message.from_user)
    update.message.reply_text(text=f"salom {update.message.from_user.first_name}")
    context.bot.send_message(chat_id=ADMIN_ID, text=f"Yangi user: {update.message.from_user.first_name}")

def main():
    TOKEN = "8062600526:AAEis5onPOo9CV15H-2abjXGH1GDC_fYF44"
    updater = Updater(token=TOKEN, request_kwargs={'connect_timeout': 30, 'read_timeout': 30})
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_cmd))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()