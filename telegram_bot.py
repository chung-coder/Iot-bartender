import logging

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# state
AGE = range(1)


def start(update: Update, context: CallbackContext) -> None:

    keyboard = [
        [
            InlineKeyboardButton(
                text="是，我滿18歲了!", callback_data="Yes"),
            InlineKeyboardButton(text="還沒，我未滿18歲", callback_data="No"),
        ],
    ]

    update.message.reply_text(
        "嗨! 我是Tender Botter，很高興能為您服務!"
    )

    update.message.reply_text(
        "請問您是否已滿18歲?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return AGE


def drinkWine(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # 使用者已成年
    if query.data == "Yes":

        keyboard = [
            [
                InlineKeyboardButton(
                    "成熟的大人 - 米咖儂", callback_data='成熟的大人 - 米咖儂'),
            ],
            [
                InlineKeyboardButton("米蔓天使 - 米蔓", callback_data='米蔓天使 - 米蔓'),
            ],
            [
                InlineKeyboardButton("少女心 - 米美雪", callback_data='少女心 - 米美雪'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text(
            text="請選擇您的調酒品項", reply_markup=reply_markup
        )

    # 使用者未成年
    elif query.data == "No":
        keyboard = [
            [
                InlineKeyboardButton(
                    "來點氣泡吧 - 雪碧", callback_data='來點氣泡吧 - 雪碧'),
            ],
            [
                InlineKeyboardButton(
                    "成熟的味道 - 伯朗咖啡", callback_data='成熟的味道 - 伯朗咖啡'),
            ],
            [
                InlineKeyboardButton("新鮮純淨 - 牛乳", callback_data='新鮮純淨 - 牛乳'),
            ],
            [
                InlineKeyboardButton("酸甜滋味 - 蔓越莓", callback_data='酸甜滋味 - 蔓越莓'),
            ],
            [
                InlineKeyboardButton("清涼果汁 - 美粒果", callback_data='清涼果汁 - 美粒果'),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text(
            text="未滿18歲禁止飲酒，請選擇您的飲品", reply_markup=reply_markup
        )

    return AGE


def main():

    updater = Updater(
        "1202208172:AAFdfP6gj-fgaRVO3t6nhvek7B7mXQPOMZQ", use_context=True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            AGE: [
                CallbackQueryHandler(drinkWine),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
