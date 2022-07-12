from datetime import *
from email import message
from pytz import *
from telegram import *
from telegram.ext import *


#Diccionario de Cumpleañeros

birthdays = {
    "12-07":["Elimelech", "Attale"],
    "29-06":["Yoandry", "ladejo"],
    "06-06":["Melvin", "Santana"],
}

#Zona del tiempo y hora

today = datetime.now(timezone('America/Caracas'))
today_string = today.strftime("%d-%m")

#Informacion Telegram Bot y Chat

API_Key = ""
CHAT_ID = ""

bot = Bot(API_Key)
updater = Updater(API_Key, use_context=True)
updater.start_polling()

if today_string in birthdays:
    message = "Hoy es el cumpleaños de\n"
    for i in birthdays[today_string]:
        message += i +'\n'

    print(message)
    bot.send_message(
        chat_id = CHAT_ID,
        text = message
    )

else:
    message = "No birthdays today."
    bot.send_message(
        chat_id = CHAT_ID,
        text = message
    )

updater.stop()