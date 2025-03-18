from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
import yt_dlp

def start(update, context):
    buttons = [
        [KeyboardButton(text="youtubedan video yuklash"),
        KeyboardButton(text="instagramdan video yuklash")]
    ]
    update.message.reply_text(text=f"salom {update.message.from_user.first_name}", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))

def youtube_handler(update, context):
    try:
        update.message.reply_text(text=update.message.text)
    except Exception as e:
        raise e

def button_handler(update, context):
    text = update.message.text

    if text == "youtubedan video yuklash":
        update.message.reply_text("video linkini yuboring...")
        return youtube_handler(update, context)
    else:
        update.message.reply_text(text="noto'g'ri buyruq kiritildi!")

def main():
    updater = Updater("8062600526:AAEis5onPOo9CV15H-2abjXGH1GDC_fYF44")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, button_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()