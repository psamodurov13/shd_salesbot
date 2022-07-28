from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink
from main import collect_data
import json
import markups as nav

bot = Bot(token='5446221087:AAEF4ERrcs36yowE7XRSZT0vXLDMnh5ZoM8', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Выберите категорию товаров', reply_markup=nav.main_keyboard)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Для женщин':
        await bot.send_message(message.from_user.id, 'Выберите нужный раздел', reply_markup=nav.woman_keyboard)
    if message.text == 'Домашняя одежда':
        await bot.send_message(message.from_user.id, 'Выберите нужный раздел', reply_markup=nav.woman_home_keyboard)
    elif message.text in nav.categories_dict:
        await bot.send_message(message.from_user.id, 'Пожалуйста, подождите...')
        collect_data(nav.categories_dict[message.text])

        with open('results.json') as file:
            data = json.load(file)

        if data == []:
            await message.answer('В данный момент скидок на товары в этой категории нет. Но '
                                 'Вы можете воспользоваться скидкой 10% на покупку от 4000 рублей. '
                                 'Используйте промокод "pt138" при оформлении заказа на сайте '
                                 'https://sweethomedress.ru/')
        else:
            for product in data:
                card = (f'{hlink(product.get("title"), product.get("url"))}\n'
                        f'{hbold("Цена до скидки: ", product.get("old_price"))}\n'
                        f'{hbold("Цена со скидкой: ", product.get("new_price"))}\n'
                        f'Размеры: {product.get("size")}\n')
                await message.answer(card)

    elif message.text == 'Главное меню':
        await message.answer('Выберите категорию товаров', reply_markup=nav.main_keyboard)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
