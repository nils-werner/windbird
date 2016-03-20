from __future__ import absolute_import
import telegram


def post(config, message):
    bot = telegram.Bot(token=config['api']['token'])
    bot.sendMessage(chat_id=config['target']['chat_id'], text=message)
