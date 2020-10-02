from config import BOT_TOKEN
import logging
from aiogram import types, Dispatcher, Bot, executor
import keyboards as kb

TOKEN = os.getenv('TOKEN', '')  # Press "Reveal Config Vars" in settings tab on Heroku and set TOKEN variable

WEBHOOK_HOST = f'https://orientation-bot.herokuapp.com/'  # Enter here your link from Heroku project settings
WEBHOOK_URL_PATH = '/webhook/' + TOKEN
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_URL_PATH)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
Message = types.message

a = 0
n = 0
b = 0


@dp.message_handler(commands=['start'])
async def hello_command(message: Message):
    with open(f'static/start.jpg', 'rb') as photo:
        await bot.send_photo(message.from_user.id, photo,
                             caption='Здравствуйте, я Ориентир Гимназии. '
                                     'Для того, чтобы Вы смогли получить меню. '
                                     'Следует просто написать или нажать /menu',
                             reply_markup=kb.help_text)
        await bot.edit_message_text(message.from_user.id, message_id=message.id)  # 1


@dp.message_handler(commands=['help'])
async def hello_command2(message: Message):
    pass


@dp.message_handler(commands=['menu'])
async def help_command(message: Message):
    await message.reply('Вот ваше меню.',
                        reply_markup=kb.orientation1)


@dp.callback_query_handler(text='orientation')
async def answer_message_btn2(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await bot.send_message(call.message.chat.id,
                           '🎓💥Отлично, выберите класс и букву класса,'
                           ' тогда мы покажем ваше расписание💥🎓')
    await bot.send_message(call.message.chat.id,
                           'Укажите класс', reply_markup=kb.how_class)
    await bot.send_message(call.message.chat.id, 'Укажите букву класса.',
                           reply_markup=kb.how_letter)


@dp.callback_query_handler(text='fast')
async def fast(message: Message):
    # await bot.edit_message_reply_markup(inline_message_id=)
    with open(f'static/fast.jpg', 'rb') as photo:
        await bot.send_photo(message.from_user.id, photo,
                             caption='🍴 Столо́вая — разновидность предприятия '
                                     'общественного питания, «общедоступное'
                                     ' или обслуживающее определённый'
                                     ' контингент '
                                     'предприятие питания, производящее'
                                     ' и реализующее '
                                     'кулинарную продукцию»[1] для получения'
                                     ' полноценного'
                                     ' питания (обеда) из трёх блюд. 🍴',
                             reply_markup=kb.fast_orientation)


@dp.callback_query_handler()
async def class_orientation(call: True):
    global a, b
    c = call.data
    if c == 'a' or c == 'b':
        b = call.data
    elif c == 'breakfast' or c == 'lunch' or c == 'afternoon_tea' or c == 'dinner' or c == 'sonnik':
        print(c)
        with open(f'static/{c}.png', 'rb') as photo:
            await bot.send_photo(call.message.chat.id, photo,
                                 caption=f'Вы выбрали {c}')
    else:
        a = call.data
    for i in range(1, 12):
        if f'{a}{b}' == f'{i}a' or f'{a}{b}' == f'{i}b':
            with open(f'static/{i}{b}.png', 'rb') as photo:
                await bot.send_photo(call.message.chat.id, photo,
                                     caption=f'✅ Отлично! Вот '
                                             f'ваше расписание на {i}'
                                             f' "{b}" класс')
                a = 0
                b = 0


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
