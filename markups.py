from aiogram import types

button_to_main = types.KeyboardButton('Главное меню')

# Main menu #
main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_buttons = ['Для женщин', 'Для мужчин', 'Для детей']
categories_dict = {
    'Для мужчин': 'Товары для мужчин',
    'Для детей': 'Детская домашняя одежда',
    'Нижнее белье': 'Нижнее белье',
    'Купальники': 'Купальники',
    'Эротическое белье': 'Эротическое белье',
    'Для спорта и отхыха': 'Женская одежда для спорта и отдыха',
    'Пижамы': 'Женские пижамы',
    'Сорочки': 'Ночные сорочки',
    'Халаты': 'Женсккие халаты',
    'Костюмы': 'Домашние костюмы',
    'Комплекты': 'Домашние комплекты',
    'Платья': 'Женские домашние платья',
    'Туники': 'Женские домашние туники'
}
main_keyboard.add(*start_buttons)

# For woman #
woman_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
woman_buttons = ['Домашняя одежда', 'Нижнее белье', 'Купальники', 'Эротическое белье', 'Для спорта и отхыха']
woman_keyboard.add(*woman_buttons, button_to_main)

# For woman home #
woman_home_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
woman_home_buttons = ['Пижамы', 'Сорочки', 'Халаты', 'Костюмы', 'Комплекты', 'Платья', 'Туники']
woman_home_keyboard.add(*woman_home_buttons, button_to_main)
