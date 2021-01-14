from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from sample.config import TG_TOKEN
from sample.config import TG_API_URL
from telegram.ext import Filters
from subprocess import Popen
from datetime import datetime
import apiai, json
from bs4 import BeautifulSoup
import requests


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Привет! Отправь мне что-нибудь',
    )

def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Это учебный бот\n'
             'Список доступных команд есть в меню\n'
             'Так же я отвечу на любое сообщение',
    )

def do_time1(bot: Bot, update: Update):
    """ Узнать время на сервере для Windows
    """
    now = datetime.now()
    text = "{}.{}.{} {}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute, now.second)
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Дата и время на сервере: \n{}".format(text),
    )

def do_echo(bot:Bot, update: Update):

        request = apiai.ApiAI('b2002bb0e47c44a1ac89baf9eab85a23').text_request()  # Токен API к Dialogflow
        request.lang = 'ru'  # На каком языке будет послан запрос
        request.session_id = 'BatlabAIBot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
        request.query = update.message.text  # Посылаем запрос к ИИ с сообщением от юзера
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
        # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
        if response:
            bot.send_message(chat_id=update.message.chat_id, text=response)
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')


def do_math_today(bot:Bot, update: Update):
    url = 'https://www.sport-express.ru/football/'
    page = requests.get(url)
    new_news = []
    news = []
    soup = BeautifulSoup(page.content, 'html.parser')
    news = soup.findAll('a', class_='se19-translation-block__match')

    # print(news)
    content = []
    for i in range(len(news)):
        if news[i].find('span', class_='se19-translation-block__cell se19-translation-block__cell--team') is not None:
            new_news.append(news[i].text)
    for i in range(len(new_news)):
        content.append(new_news[i])

    bot.send_message(
        chat_id=update.message.chat_id,
        text=("Сегодня играют:\n{}".format(content),),
    )

def main():
    bot= Bot(
        token=TG_TOKEN,
        base_url= TG_API_URL,
    )
    updater= Updater(
        bot=bot,
    )
    start_handler= CommandHandler('start', do_start )
    message_handler = MessageHandler(Filters.text, do_echo)
    help_handler = CommandHandler('help', do_help)
    today_handler= CommandHandler('today', do_math_today)
    time1_handler = CommandHandler("time", do_time1)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(today_handler)


    updater.dispatcher.add_handler(time1_handler)

    updater.start_polling()
    updater.idle()

if __name__ =='__main__':
    main()

