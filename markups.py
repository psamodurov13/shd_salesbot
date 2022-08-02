from aiogram import types

button_to_main = types.InlineKeyboardButton(text='Главное меню', callback_data='Главное меню')

# Main menu #
main_keyboard = types.InlineKeyboardMarkup()
for_woman = types.InlineKeyboardButton(text='Для женщин', callback_data='Для женщин')
for_man = types.InlineKeyboardButton(text='Для мужчин', callback_data='Для мужчин')
for_kids = types.InlineKeyboardButton(text='Для детей', callback_data='Для детей')
categories_dict = {
    'Для мужчин': ['Товары для мужчин', 'https://sweethomedress.ru/dlya-muzhchin/skidka/tovar-so-skidkoj/'],
    'Для детей': ['Детская домашняя одежда', 'https://sweethomedress.ru/dlya-detey/skidka/tovar-so-skidkoj/'],
    'Нижнее белье': ['Нижнее белье', 'https://sweethomedress.ru/nizhnee-belye/skidka/tovar-so-skidkoj/'],
    'Купальники': ['Купальники', 'https://sweethomedress.ru/kupalniki/skidka/tovar-so-skidkoj/'],
    'Эротическое белье': ['Эротическое белье',
                          'https://sweethomedress.ru/eroticheskoye-belye/skidka/tovar-so-skidkoj/'],
    'Для спорта и отхыха': ['Женская одежда для спорта и отдыха',
                            'https://sweethomedress.ru/fitnes/skidka/tovar-so-skidkoj/'],
    'Пижамы': ['Женские пижамы', 'https://sweethomedress.ru/katalog/pizhamy/skidka/tovar-so-skidkoj/'],
    'Сорочки': ['Ночные сорочки', 'https://sweethomedress.ru/katalog/nochnye-sorochki/skidka/tovar-so-skidkoj/'],
    'Халаты': ['Женсккие халаты', 'https://sweethomedress.ru/katalog/halaty/skidka/tovar-so-skidkoj/'],
    'Костюмы': ['Домашние костюмы', 'https://sweethomedress.ru/katalog/kostumy/skidka/tovar-so-skidkoj/'],
    'Комплекты': ['Домашние комплекты', 'https://sweethomedress.ru/katalog/komplekty/skidka/tovar-so-skidkoj/'],
    'Платья': ['Женские домашние платья', 'https://sweethomedress.ru/katalog/platja/skidka/tovar-so-skidkoj/'],
    'Туники': ['Женские домашние туники', 'https://sweethomedress.ru/katalog/tuniki/skidka/tovar-so-skidkoj/']
}
main_keyboard.add(for_woman, for_man, for_kids)

# For woman #
woman_keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
woman_buttons = ['Домашняя одежда', 'Нижнее белье', 'Купальники', 'Эротическое белье', 'Для спорта и отхыха']
woman_keyboard.add(*[types.InlineKeyboardButton(text=i, callback_data=i) for i in woman_buttons], button_to_main)

# For woman home #
woman_home_keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
woman_home_buttons = ['Пижамы', 'Сорочки', 'Халаты', 'Костюмы', 'Комплекты', 'Платья', 'Туники']
woman_home_keyboard.add(*[types.InlineKeyboardButton(text=i, callback_data=i) for i in woman_home_buttons], button_to_main)


def view(category):
    view_keyboard = types.InlineKeyboardMarkup(row_width=1)
    view_button_site = types.InlineKeyboardButton(text='Посмотреть список на сайте', callback_data='1'+category)
    view_button_tb = types.InlineKeyboardButton(text='Прислать ссылки в чат', callback_data='2'+category)
    view_keyboard.add(view_button_site, view_button_tb, button_to_main)
    return view_keyboard


def create_link_keyboard(category):
    link_keyboard = types.InlineKeyboardMarkup()
    link_key = types.InlineKeyboardButton(text=category, url=categories_dict[category][1])
    link_keyboard.add(link_key, button_to_main)
    return link_keyboard
