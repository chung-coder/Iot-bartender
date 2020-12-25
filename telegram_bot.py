import logging
import json
import qrcode
from PIL import Image
from io import BytesIO

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# state
CHOOSE, RATIO, SHOWING = range(3)


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

    return CHOOSE


def drinkWine(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # 使用者已成年
    if query.data == "Yes":

        keyboard = [
            [
                InlineKeyboardButton(
                    "成熟的大人 - 米咖儂", callback_data='wine_1'),
            ],
            [
                InlineKeyboardButton("米蔓天使 - 米蔓", callback_data='wine_2'),
            ],
            [
                InlineKeyboardButton("少女心 - 米美雪", callback_data='wine_3'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text(
            text="請選擇您的調酒品項", reply_markup=reply_markup
        )

    # 使用者未成年
    elif query.data == "No":
        drink_1 = json.dumps(
            {"type": "drink_1", "ratio": "regular"}, indent=4)
        drink_2 = json.dumps(
            {"type": "drink_2", "ratio": "regular"}, indent=4)
        drink_3 = json.dumps(
            {"type": "drink_3", "ratio": "regular"}, indent=4)
        drink_4 = json.dumps(
            {"type": "drink_4", "ratio": "regular"}, indent=4)
        drink_5 = json.dumps(
            {"type": "drink_5", "ratio": "regular"}, indent=4)

        keyboard = [
            [
                InlineKeyboardButton(
                    "來點氣泡吧 - 雪碧", callback_data=drink_1),
            ],
            [
                InlineKeyboardButton(
                    "成熟的味道 - 伯朗咖啡", callback_data=drink_2),
            ],
            [
                InlineKeyboardButton("新鮮純淨 - 牛乳", callback_data=drink_3),
            ],
            [
                InlineKeyboardButton("酸甜滋味 - 蔓越莓汁", callback_data=drink_4),
            ],
            [
                InlineKeyboardButton("清涼果汁 - 美粒果", callback_data=drink_5),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text(
            text="未滿18歲禁止飲酒，請選擇您的飲品", reply_markup=reply_markup
        )
        return SHOWING

    return RATIO


def ratio(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    low = json.dumps(
        {"type": query.data, "ratio": "low"}, indent=4)
    medium = json.dumps(
        {"type": query.data, "ratio": "medium"}, indent=4)
    high = json.dumps(
        {"type": query.data, "ratio": "high"}, indent=4)

    if(query.data.find("wine") == 0):
        keyboard = [
            [
                InlineKeyboardButton(
                    "低濃度", callback_data=low),
            ],
            [
                InlineKeyboardButton("黃金比例", callback_data=medium),
            ],
            [
                InlineKeyboardButton("高濃度", callback_data=high),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(
        text="請選擇您的酒精濃度", reply_markup=reply_markup
    )

    return SHOWING


def show_data(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = json.loads(query.data)

    # 飲品種類字典
    state_type = {"wine_1": "成熟的大人 - 米咖儂",
                  "wine_2": "米蔓天使 - 米蔓",
                  "wine_3": "少女心 - 米美雪",
                  "drink_1": "來點氣泡吧 - 雪碧",
                  "drink_2": "成熟的味道 - 伯朗咖啡",
                  "drink_3": "新鮮純淨 - 牛乳",
                  "drink_4": "酸甜滋味 - 蔓越莓汁",
                  "drink_5": "清涼果汁 - 美粒果",
                  }
    # 濃度字典

    state_ratio = {"regular": "無酒精成分",
                   "low": "低濃度",
                   "medium": "黃金比例",
                   "high": "高濃度",
                   }

    query.edit_message_text(
        text="以下是您選擇的飲品:\n"+"\n飲品種類: " +
        state_type[data["type"]] + "\n\n飲品濃度: " + state_ratio[data["ratio"]],
    )

    # 產生QRcode並回傳telegram-bot
    img = qrcode.make(data)
    bio = BytesIO()
    bio.name = 'image.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    query.bot.send_photo(chat_id=update.effective_chat.id, photo=bio)


def main():

    updater = Updater(
        "1202208172:AAFdfP6gj-fgaRVO3t6nhvek7B7mXQPOMZQ", use_context=True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSE: [CallbackQueryHandler(drinkWine), ],
            RATIO: [CallbackQueryHandler(ratio), ],
            SHOWING: [CallbackQueryHandler(show_data), ]

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
