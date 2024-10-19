import telebot
from telebot import types
from translate import Translator

bot = telebot.TeleBot('5286679755:AAEPd3jJAma3LUCd85EWbg0Hy4rYU3Zu1Vc')

@bot.message_handler(commands=["start"])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Перевод', callback_data='Translation'))
    bot.send_message(message.chat.id, "Привет! Я бот-переводчик и готов переводить твои фразы.",
                     reply_markup=markup)


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    bot.answer_callback_query(callback_query_id=call.id)
    if call.data == 'Translation':
        markup = types.InlineKeyboardMarkup()
        item_1 = types.InlineKeyboardButton(text = 'Russian', callback_data='Other')
        item_2 = types.InlineKeyboardButton(text = 'French', callback_data='Other')
        item_3 = types.InlineKeyboardButton(text='German', callback_data='Other')
        item_4 = types.InlineKeyboardButton(text='Japanese', callback_data='Other')
        item_5 = types.InlineKeyboardButton(text='Chinese', callback_data='Other')

        markup.add(item_1, item_2, item_3, item_4, item_5)
        bot.send_message(call.message.chat.id, 'Выберите язык, на который надо перевести', reply_markup=markup)
    elif call.data == 'Other':
        markup_r = types.InlineKeyboardMarkup()
        item_6 = types.InlineKeyboardButton(text = 'Выбрать другой язык', callback_data='Translation')
        markup_r.add(item_6)
        bot.send_message(call.message.chat.id, 'Ещё вы можете', reply_markup=markup_r)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Russian':
        mesg = bot.send_message(message.chat.id, 'Введите текст')
        bot.register_next_step_handler(mesg, trans_1)
    if message.text == 'French':
        mesg = bot.send_message(message.chat.id, 'Введите текст')
        bot.register_next_step_handler(mesg, trans_2)
    if message.text == 'German':
        mesg = bot.send_message(message.chat.id, 'Введите текст')
        bot.register_next_step_handler(mesg, trans_3)
    if message.text == 'Japanese':
        mesg = bot.send_message(message.chat.id, 'Введите текст')
        bot.register_next_step_handler(mesg, trans_4)
    if message.text == 'Chinese':
        mesg = bot.send_message(message.chat.id, 'Введите текст')
        bot.register_next_step_handler(mesg, trans_5)


def trans_1(message):
    translator = Translator(to_lang='Russian')
    word = translator.translate(message.text)
    bot.send_message(message.chat.id, word)


def trans_2(message):
    translator = Translator(to_lang='French')
    word = translator.translate(message.text)
    bot.send_message(message.chat.id, word)


def trans_3(message):
    translator = Translator(to_lang='German')
    word = translator.translate(message.text)
    bot.send_message(message.chat.id, word)


def trans_4(message):
    translator = Translator(to_lang='Japanese')
    word = translator.translate(message.text)
    bot.send_message(message.chat.id, word)


def trans_5(message):
    translator = Translator(to_lang='Chinese')
    word = translator.translate(message.text)
    bot.send_message(message.chat.id, word)


bot.polling(none_stop=True)
