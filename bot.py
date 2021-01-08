import telebot
import config
import parse
import weather
import random
from telebot import types

# Присвоение переменной бот токена
bot = telebot.TeleBot(config.TOKEN)


# Функция для получения ответа погоды с сервера
def weather_message(message):
    answer = weather.get_weath(message)
    bot.send_message(message.chat.id, answer, parse_mode='html')


# Обработчик команд '/start' 
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBv8lf-FcYFKkHTTfHn-H7-TrXQptKlQACAQEAAladvQoivp8OuMLmNB4E')

    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создаем объект, изменяем его размер
    # Кнопки клавиатуры
    btn1 = types.KeyboardButton("Стикеры")
    btn2 = types.KeyboardButton("Картинки")
    btn3 = types.KeyboardButton("Погода")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n Я - <b>{1.first_name}</b>, бот созданный по-приколу, исключительно в учебно-развекательных целях.\nЯ могу предложить Вам уникальный набор стикеров, отправить забавную картиночку или даже подсказать погоду".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# Обработчик команд '/help'
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Ваш ID: {0.id}".format(message.from_user), parse_mode='html')


# Обработчик повторения текста
@bot.message_handler(content_types=['text'])
def dialog_message(message):
    if message.chat.type == 'private':
        if message.text == 'Стикеры':
            # создаем объект, изменяем его размер
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Лучик", callback_data='stick')

            markup.add(item1)
            # Прицепляем инлайновую клавиатуру к сообщению
            bot.send_message(message.chat.id, "Пока доступен только один вариант стикеров", reply_markup=markup)
        if message.text == 'Картинки':
            # создаем объект, изменяем его размер
            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton("Хорошего настроения", callback_data='img1')
            item4 = types.InlineKeyboardButton("Хорошего дня", callback_data='img2')
            item5 = types.InlineKeyboardButton("Доброго утра", callback_data='img3')
            item6 = types.InlineKeyboardButton("Спокойной ночи", callback_data='img4')

            markup.add(item3, item4, item5, item6)
            # Прицепляем инлайновую клавиатуру к сообщению
            bot.send_message(message.chat.id,
                             "В этом разделе я могу отправить тебе картинки.\nКакая тематика пожеланий тебя больше интересует?"
                             , reply_markup=markup, parse_mode='html')
        if message.text == 'Погода':
            city = bot.send_message(message.chat.id, "В каком городе Вам показать погодку?")
            bot.register_next_step_handler(city, weather_message)
        else:
            bot.send_message(message.chat.id, message.text)


def markup_item(data):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton("Следующая", callback_data=data)
    markup.add(item)
    return markup


# Обработка нажатия кнопки инлайновой клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'stick':
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEBiQVfoojOYUDSwB9AE0QlQzpFPJZFgQACDQADgZpkHFkF6lQ08yteHgQ')
                bot.send_message(call.message.chat.id,
                                 "{0.first_name} хочет предложить тебе уникальный набор стикеров!\nДанный набор был нарисован начинающим дизайнером <b>Полиной Соловьёвой</b>!Перейдя по этой ссылке ты сможешь добавить их себе: https://t.me/addstickers/PolySunray".format(
                                     call.message.from_user)
                                 , parse_mode='html')

            elif call.data == 'img1':
                markup_item(call.data)
                comps = parse.parse(call.data)
                random_comp = random.choice(comps)
                parse.load_image(random_comp)
                img = open('out.jpg', 'rb')
                bot.send_photo(call.message.chat.id, img, caption=random_comp["title"],
                               reply_markup=markup_item(call.data))

            elif call.data == 'img2':
                markup_item(call.data)
                comps = parse.parse(call.data)
                random_comp = random.choice(comps)
                parse.load_image(random_comp)
                img = open('out.jpg', 'rb')
                bot.send_photo(call.message.chat.id, img, caption=random_comp["title"],
                               reply_markup=markup_item(call.data))
            elif call.data == 'img3':
                markup_item(call.data)
                comps = parse.parse(call.data)
                random_comp = random.choice(comps)
                parse.load_image(random_comp)
                img = open('out.jpg', 'rb')
                bot.send_photo(call.message.chat.id, img, caption=random_comp["title"],
                               reply_markup=markup_item(call.data))
            elif call.data == 'img4':
                markup_item(call.data)
                comps = parse.parse(call.data)
                random_comp = random.choice(comps)
                parse.load_image(random_comp)
                img = open('out.jpg', 'rb')
                bot.send_photo(call.message.chat.id, img, caption=random_comp["title"],
                               reply_markup=markup_item(call.data))

    except Exception as e:
        print(repr(e))


# Запуск
bot.polling(none_stop=True)
