import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("成熟的大人 - 米咖儂", callback_data='成熟的大人 - 米咖儂'),
        ],
        [
            InlineKeyboardButton("米蔓天使 - 米蔓", callback_data='米蔓天使 - 米蔓'),
        ],
        [
            InlineKeyboardButton("少女心 - 米美雪", callback_data='少女心 - 米美雪'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('請選擇你的調酒:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    query.edit_message_text(text=f"你選擇的調酒是 {query.data}")


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("輸入 /start 開始調酒")


def main():

    updater = Updater(
        "my-token", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
