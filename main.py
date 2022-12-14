from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Text
from loguru import logger
from aiogram.utils.markdown import hbold, hlink
from functions import collect_data, get_urls, get_prod_info
import markups as nav
import os

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation='10 KB', compression='zip')
token = os.getenv("TOKEN")
bot = Bot(token='token', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Выберите категорию товаров', reply_markup=nav.main_keyboard)

cb = CallbackData('prod', 'action', 'category')


@dp.callback_query_handler(lambda callback: callback.data in ['Для женщин', 'Домашняя одежда', 'Главное меню'])
async def bot_callback(callback: types.CallbackQuery):
    if callback.data == 'Для женщин':
        await bot.send_message(callback.message.chat.id, 'Выберите нужный раздел', reply_markup=nav.woman_keyboard)
    elif callback.data == 'Домашняя одежда':
        await bot.send_message(callback.message.chat.id, 'Выберите нужный раздел', reply_markup=nav.woman_home_keyboard)
    elif callback.data == 'Главное меню':
        await callback.message.answer('Выберите категорию товаров', reply_markup=nav.main_keyboard)


@dp.callback_query_handler(lambda callback: callback.data in nav.categories_dict)
async def choice_type(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, 'Хотите посмотреть список товаров на сайте или прислать ссылки на товары в чат?',
                           reply_markup=nav.view(callback.data))


@logger.catch
@dp.callback_query_handler(Text(startswith='1'))
async def link_sale(call: types.CallbackQuery):
    await call.message.answer('Перейти на сайт: ', reply_markup=nav.create_link_keyboard(call.data[1:]))
    await call.answer()


@dp.callback_query_handler(Text(startswith='2'))
async def link_sale(call: types.CallbackQuery):
    await call.message.answer('Пожалуйста, подождите...')
    pages = collect_data(nav.categories_dict[call.data[1:]][1])
    if pages > 0:
        count = 0
        for page in range(1, pages + 1):
            if count == 10:
                break
            else:
                products = get_urls(nav.categories_dict[call.data[1:]][1], page)
                card_param = get_prod_info(products, nav.categories_dict[call.data[1:]])
                for i in range(10):
                    card_info = next(card_param)
                    card = (f'{hlink(card_info[0], card_info[1])}\n'
                            f'{hbold("Цена до скидки: ", card_info[2])}\n'
                            f'{hbold("Цена со скидкой: ", card_info[3])}\n'
                            f'Размеры: {card_info[4]}\n')
                    await call.message.answer(card)
                    count += 1
                    if count == 10:
                        break
                await call.message.answer('Все товары со скидками пожно посмотреть на сайте')
                await call.message.answer('Перейти на сайт: ', reply_markup=nav.create_link_keyboard(call.data[1:]))
    else:
        await call.message.answer('К сожалению в данный момент товаров со скидкой в выбранном разделе нет. '
                                  'Но Вы можете воспользоваться промокодом "tg1991" на скидку 10%. Скидка '
                                  'действует при покупке от 4000 рублей. Перейти на сайт можно по ссылке '
                                  'https://sweethomedress.ru')
    await call.message.answer('Выберите категорию товаров', reply_markup=nav.main_keyboard)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
