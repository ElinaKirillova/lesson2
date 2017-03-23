import operator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from wordcounted import wordcounted


def greet_user (bot, update):
    print('/start')
    print('/wordcount')
    print (update)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def wordcount(bot, update):
    count = wordcounted(update.message.text)
    bot.sendMessage(update.message.chat_id, text = 'В вашей фразе {0} слов(а)'.format(count))

def count_it(bot, update):
    text = update.message.text
    text = text[9:]

    actions = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul,
        '/': operator.truediv,
    }

    for action_sign in actions:
        if action_sign in text:
            action = action_sign

    if action == '/' and text.split(action)[1] == '0':
        result = 'На ноль делить нелья'
    else:
        result = actions[action](
            int(text.split(action)[0]),
            int(text.split(action)[1]),
        )


    # if '-' in text:
    #     a, b = text.split('-')
    #     result = a - b
    # elif '+' in text:
    #     a, b = text.split('+')
    #     result = a + b
    # elif '*' in text:
    #     a, b = text.split('*')
    #     result = a * b
    # elif '/' in text:
    #     a, b = text.split('/')
    #     result = a / b

    bot.sendMessage(update.message.chat_id, text=result)


def show_error (bot, update, error):
    print(error)

def talk_to_me (bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, text='Простите, моя твоя не понимать')

def main():
    updater = Updater("360489355:AAFgZrrBE09UYuAUJedvos47V29Vb4sGPrU")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("count_it", count_it))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()


main()
