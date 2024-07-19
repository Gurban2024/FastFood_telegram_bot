import aiogram
from aiogram import filters, types, Bot, Dispatcher, F
import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import re


class Reg(StatesGroup):
    contact = State()


class Cards(StatesGroup):
    humo = State()  
    uzcard = State()


bot = Bot(token='7429834785:AAFfTbGIkbifAkdMqAKjN_QYJrH5q7ewnMw')
dp = Dispatcher(bot=bot)

grocery_basket = []

contact_buttons1 = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Отправить контакт', request_contact=True)]],
    resize_keyboard=True
)

back2 = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='🔙 Назад')]],
    resize_keyboard=True
)

drink_food1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Еда'), KeyboardButton(text='Напитки')],
        [KeyboardButton(text='🔙 Назад')]
    ],
    resize_keyboard=True
)

food1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🫓 Лаваш')],
        [KeyboardButton(text='🌭 Хот-дог'), KeyboardButton(text='🍕 Пицца')],
        [KeyboardButton(text='🥪 Сэндвич'), KeyboardButton(text='🌮 Тако')],
        [KeyboardButton(text='🍜 Суп')],
        [KeyboardButton(text='🔙 Назад')]
    ],
    resize_keyboard=True
)

drink1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🥤 Вода')],
        [KeyboardButton(text='🍹 Смузи'), KeyboardButton(text='🍵 Зеленый чай')],
        [KeyboardButton(text='🫖 Черный чай'), KeyboardButton(text='🧋 Боба чай')],
        [KeyboardButton(text='☕ Коффе')],
        [KeyboardButton(text='🔙 Назад')]
    ],
    resize_keyboard=True
)

sure1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✔️ Да'), KeyboardButton(text='❌ Нет')]
    ],
    resize_keyboard=True
)

main_menu1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🍽 Меню')],
        [KeyboardButton(text='🛒 Корзина'), KeyboardButton(text='ℹ️ О нас')],
        [KeyboardButton(text='👤 Моя информация'), KeyboardButton(text='🆘 Поддержка')],
        [KeyboardButton(text='🌐 Изменить язык')]
    ],
    resize_keyboard=True
)

languages1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🗽 Английский', callback_data='english'),
         InlineKeyboardButton(text='🪆 Русский', callback_data='russian')]
    ],
    resize_keyboard=True
)

buy_buttons1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✔️ Купить всё'), KeyboardButton(text='❌ Очистить корзину')],
        [KeyboardButton(text='⬅️ Назад')]
    ],
    resize_keyboard=True
)

cards1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Humo', callback_data='humo'),
         InlineKeyboardButton(text='UzCard', callback_data='uzcard')]
    ],
    resize_keyboard=True
)

contact_buttons = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Send your Contact', request_contact=True)]],
    resize_keyboard=True
)

back1 = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='🔙 Back')]],
    resize_keyboard=True
)

drink_food = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Food'), KeyboardButton(text='Drink')],
        [KeyboardButton(text='🔙 Back')]
    ],
    resize_keyboard=True
)

food = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🫓 Lavash')],
        [KeyboardButton(text='🌭 Hotdog'), KeyboardButton(text='🍕 Pizza')],
        [KeyboardButton(text='🥪 Sandvich'), KeyboardButton(text='🌮 Taco')],
        [KeyboardButton(text='🍜 Soup')],
        [KeyboardButton(text='🔙 Back')]
    ],
    resize_keyboard=True
)

drink = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🥤 Water')],
        [KeyboardButton(text='🍹 Smoozy'), KeyboardButton(text='🍵 Green Tea')],
        [KeyboardButton(text='🫖 Black Tea'), KeyboardButton(text='🧋 Bubble Tea')],
        [KeyboardButton(text='☕ Coffe')],
        [KeyboardButton(text='🔙 Back')]
    ],
    resize_keyboard=True
)

sure = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✔️ Yes'), KeyboardButton(text='❌ No')]
    ],
    resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Menu')],
        [KeyboardButton(text='Grocery Basket'), KeyboardButton(text='About Us')],
        [KeyboardButton(text='My Information'), KeyboardButton(text='Support')],
        [KeyboardButton(text='Change Language')]
    ],
    resize_keyboard=True
)

languages = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🗽 English Language', callback_data='english'),
         InlineKeyboardButton(text='🪆 Русский Язык', callback_data='russian')]
    ],
    resize_keyboard=True
)

buy_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✔️ Buy All Things'), KeyboardButton(text='❌ Clear Basket')],
        [KeyboardButton(text='⬅️ Back')]
    ],
    resize_keyboard=True
)

cards = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Humo', callback_data='humo'),
         InlineKeyboardButton(text='UzCard', callback_data='uzcard')]
    ],
    resize_keyboard=True
)


@dp.message(filters.Command("start"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Reg.contact)
    await message.answer("Let\'s Start Registration | Давайте начнём регистрацию", reply_markup=contact_buttons)


@dp.message(Reg.contact)
async def send_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.contact)
    await message.answer(
        'Your Registration is Done. Pls choose language | Ваша регистрация закончилась. Пожалуйста выберите язык ',
        reply_markup=languages)
    await state.clear()


@dp.callback_query(F.data == 'russian')
async def russian_callback(call: types.CallbackQuery):
    await call.message.answer('Выберите опцию.', reply_markup=main_menu1)


@dp.message(F.text == '🔙 Назад')
async def main_back1(message: types.Message):
    await message.answer('Вы вернулись', reply_markup=main_menu1)


@dp.message(F.text == 'ℹ️ О нас')
async def show_about_us1(message: types.Message):
    await message.answer(
        'Добро пожаловать в "Быстрое удовольствие" - кафе фастфуда, где встречается быстрота и качество! Наше кафе предлагает широкий выбор аппетитных и удовлетворяющих блюд, которые приготовлены с любовью и заботой. При посещении "Быстрого удовольствия" вы сразу почувствуете уютную атмосферу и приветливую обстановку. Наша команда профессиональных поваров стремится к совершенству в каждом блюде, чтобы удовлетворить самых взыскательных гурманов.',
        reply_markup=back2)


@dp.message(F.text == '🌐 Изменить язык')
async def show_men1u(message: types.Message):
    await message.answer("Выберите язык 🤗", reply_markup=languages)


@dp.message(F.text == '👤 Моя информация')
async def show_info1(message: types.Message):
    user = message.from_user
    first_name = user.first_name
    last_name = user.last_name
    user_id = user.id

    await message.answer(f"Имя: {first_name}\nФамилия: {last_name}\nID пользователя: {user_id}", reply_markup=back2)


@dp.message(F.text == '🆘 Поддержка')
async def show_suppor1t(message: types.Message):
    await message.answer('Если у вас возникли проблемы, напишите сюда --> @fptinker', reply_markup=back2)


@dp.message(F.text == '🍽 Меню')
async def show_menu1(message: types.Message):
    await message.answer('Выберите, что вам нужно', reply_markup=drink_food1)


@dp.message(F.text == 'Еда')
async def show_food1(message: types.Message):
    await message.answer('Выберите позиции', reply_markup=food1)


@dp.message(F.text == 'Напитки')
async def show_drink1(message: types.Message):
    await message.answer('Выберите позиции', reply_markup=drink1)


@dp.message(F.text == '🫓 Лаваш')
async def lavash1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://www.restoran-shafran.uz/image/cache/catalog/product/lavash-v-tandire-i-s-sirom-2-750x500.jpg',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🌭 Хот-дог')
async def hotdog1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://www.retail.ru/upload/content/pressreleases/9d7/10590ljvybo5pae5uw24nqeisf350qfx.png',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🍜 Суп')
async def soup1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://avatars.dzeninfra.ru/get-zen_doc/1658056/pub_622ca738acc1c97a92fc6c5c_622ca7b9f53aef1fffd84c73/scale_1200',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🥪 Sandvich')
async def soup1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(photo='https://s1.eda.ru/StaticContent/Photos/170228123352/210430170814/p_O.jpg',
                               caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🍕 Пицца')
async def pizza1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://cdnn21.img.ria.ru/images/98976/61/989766135_0:105:2000:1230_1920x0_80_0_0_16a8fff0f23e9297155772f93b403aed.jpg',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🌮 Тако')
async def taco1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://avatars.dzeninfra.ru/get-zen_doc/8866523/pub_6489c8af5208a65c040f18a0_6489c8b5e7e228426ac1330f/scale_1200',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🥤 Вода')
async def water1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://navruzint.com/wp-content/uploads/2023/02/sparkling_15-2.png',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🍹 Смузи')
async def beer1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://static.1000.menu/img/content-v2/cb/1d/58130/fruktovyi-smuzi-v-blendere_1629916238_11_max.jpg',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '☕ Коффе')
async def wine1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://pudov.ru/upload/resize_cache/webp/resize_cache/iblock/020/715_500_1/o51678i5ueznfsb9e1vym01mlxvva0nd.webp',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🍵 Зеленый чай')
async def green_tea1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://d2jx2rerrg6sh3.cloudfront.net/images/news/ImageForNews_755721_16914865403343161.jpg',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🫖 Черный чай')
async def black_tea1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(photo='https://mehtaperturk.com/wp-content/uploads/2022/04/turkish-tea.jpg.webp',
                               caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '🧋 Боба чай')
async def bubble_tea1(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://cdn.shopify.com/s/files/1/2625/9204/files/bbt101_1024x1024.jpg?v=1540043903',
        caption='Вы уверены?', reply_markup=sure1)


@dp.message(F.text == '✔️ Да')
async def yes1(message: types.Message):
    await message.answer('Вы добавили этот продукт в корзину', reply_markup=drink_food1)


@dp.message(F.text == '❌ Нет')
async def no1(message: types.Message):
    grocery_basket.pop()
    await message.answer('Попробуйте найти что-то еще', reply_markup=drink_food1)


@dp.message(F.text == '🛒 Корзина')
async def basket1(message: types.Message):
    await message.answer(f'Ваша корзина: {grocery_basket}')
    await message.answer(f'Хотите купить все продукты?', reply_markup=buy_buttons1)


@dp.message(F.text == '✔️ Купить всё')
async def buy_all_thing1(message: types.Message):
    await message.answer('Пожалуйста, выберите свою карту', reply_markup=cards1)


@dp.callback_query(F.data == 'humo')
async def cart_humo1(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Cards.humo)
    await call.message.answer('Введите номер вашей карты Humo')


@dp.message(Cards.humo)
async def send_humo_card1(message: types.Message, state: FSMContext):
    card_number = message.text.strip()
    if re.match(r'^\d+$', card_number):
        await state.update_data(humo=card_number)
        await message.answer('Ваш заказ доставляется!', reply_markup=main_menu1)
        await state.clear()
    else:
        await message.answer('Пожалуйста, введите правильный номер карты (только цифры).')


@dp.callback_query(F.data == 'uzcard')
async def cart_uzcard1(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Cards.uzcard)
    await call.message.answer('Введите номер вашей карты UzCard')


@dp.message(Cards.uzcard)
async def send_uzcard1(message: types.Message, state: FSMContext):
    card_number = message.text.strip()
    if re.match(r'^\d+$', card_number):
        await state.update_data(cart_uzcard=card_number)
        await message.answer('Ваш заказ доставляется!', reply_markup=main_menu1)
        await state.clear()
    else:
        await message.answer('Пожалуйста, введите правильный номер карты (только цифры).')


@dp.message(F.text == '❌ Очистить корзину')
async def clear_basket1(message: types.Message):
    grocery_basket.clear()
    await message.answer('Ваша корзина очищена', reply_markup=main_menu1)


@dp.message(F.text == '⬅️ Назад')
async def double_back1(message: types.Message):
    await message.answer('Вы вернулись обратно', reply_markup=main_menu1)


@dp.callback_query(F.data == 'english')
async def english_callback(call: types.CallbackQuery):
    await call.message.answer('Choose option.', reply_markup=main_menu)


@dp.message(F.text == '🔙 Back')
async def main_back(message: types.Message):
    await message.answer('You Came Back', reply_markup=main_menu)


@dp.message(F.text == 'About Us')
async def show_about_us(message: types.Message):
    await message.answer(
        'A bag that impresses! Within a year she became unsurpassed in her field. Discover the most impressive and innovative experience. We offer unique opportunities and incredible results. Join us and become part of the best!',
        reply_markup=back1)


@dp.message(F.text == 'Change Language')
async def show_menu(message: types.Message):
    await message.answer("Choose the language 🤗", reply_markup=languages)


@dp.message(F.text == 'My Information')
async def show_info(message: types.Message):
    user = message.from_user
    first_name = user.first_name
    last_name = user.last_name
    user_id = user.id

    await message.answer(f"First Name: {first_name}\nLast Name: {last_name}\nUser ID: {user_id}", reply_markup=back1)


@dp.message(F.text == 'Support')
async def show_support(message: types.Message):
    await message.answer('If you have problems write here --> @fptinker', reply_markup=back1, )


@dp.message(F.text == 'Menu')
async def show_menu(message: types.Message):
    await message.answer('Choose what you want', reply_markup=drink_food, )


@dp.message(F.text == 'Food')
async def show_food(message: types.Message):
    await message.answer('Choose positions', reply_markup=food)


@dp.message(F.text == 'Drink')
async def show_food(message: types.Message):
    await message.answer('Choose positions', reply_markup=drink)


@dp.message(F.text == '🫓 Lavash')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://www.restoran-shafran.uz/image/cache/catalog/product/lavash-v-tandire-i-s-sirom-2-750x500.jpg',
        caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '🌭 Hotdog')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://www.retail.ru/upload/content/pressreleases/9d7/10590ljvybo5pae5uw24nqeisf350qfx.png',
        caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '🍜 Soup')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://avatars.dzeninfra.ru/get-zen_doc/1658056/pub_622ca738acc1c97a92fc6c5c_622ca7b9f53aef1fffd84c73/scale_1200',
        caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '🍕 Pizza')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://cdnn21.img.ria.ru/images/98976/61/989766135_0:105:2000:1230_1920x0_80_0_0_16a8fff0f23e9297155772f93b403aed.jpg',
        caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '🌮 Taco')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://avatars.dzeninfra.ru/get-zen_doc/8866523/pub_6489c8af5208a65c040f18a0_6489c8b5e7e228426ac1330f/scale_1200',
        caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '🥤 Water')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://navruzint.com/wp-content/uploads/2023/02/sparkling_15-2.png', caption='You Sure?',
        reply_markup=sure)


@dp.message(F.text == '🍹 Smoozy')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://static.1000.menu/img/content-v2/cb/1d/58130/fruktovyi-smuzi-v-blendere_1629916238_11_max.jpg',
        caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '☕ Coffe')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://www.osteria.ru/upload/iblock/d45/j3w7ifjxf4u8lqq0a7ivg1oj95ilemus/DSC02540.jpg',
        caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '🍵 Green Tea')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://d2jx2rerrg6sh3.cloudfront.net/images/news/ImageForNews_755721_16914865403343161.jpg',
        caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '🫖 Black Tea')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(photo='https://mehtaperturk.com/wp-content/uploads/2022/04/turkish-tea.jpg.webp',
                               caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '🧋 Bubble Tea')
async def lavash(message: types.Message):
    grocery_basket.append(message.text)
    await message.answer_photo(
        photo='https://cdn.shopify.com/s/files/1/2625/9204/files/bbt101_1024x1024.jpg?v=1540043903',
        caption='You Sure?', reply_markup=sure)


@dp.message(F.text == '✔️ Yes')
async def lavash(message: types.Message):
    await message.answer('You Add to Buscket this product', reply_markup=drink_food)


@dp.message(F.text == '❌ No')
async def lavash(message: types.Message):
    await message.answer('Try find something else', reply_markup=drink_food)


@dp.message(F.text == 'Grocery Basket')
async def basket(message: types.Message):
    await message.answer(f'Your products{grocery_basket}')
    await message.answer(f'You wanna buy all produts?', reply_markup=buy_buttons)


@dp.message(F.text == '✔️ Buy All Things')
async def buy_all_thing(message: types.Message):
    await message.answer('Please choose your cart', reply_markup=cards)


@dp.callback_query(F.data == 'humo')
async def cart_humo(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Cards.humo)
    await call.message.answer('Enter your Humo card number')


@dp.message(Cards.humo)
async def send_humo_card(message: types.Message, state: FSMContext):
    card_number = message.text.strip()
    if re.match(r'^\d+$', card_number):
        await state.update_data(humo=card_number)
        await message.answer('Your food is delivering!', reply_markup=main_menu)
        await state.clear()
    else:
        await message.answer('Please enter a valid card number (digits only).')


@dp.callback_query(F.data == 'uzcard')
async def cart_uzcard(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Cards.uzcard)
    await call.message.answer('Enter your UzCard number')


@dp.message(Cards.uzcard)
async def send_uzcard(message: types.Message, state: FSMContext):
    card_number = message.text.strip()
    if re.match(r'^\d+$', card_number):
        await state.update_data(cart_uzcard=card_number)
        await message.answer('Your food is delivering!', reply_markup=main_menu)
        await state.clear()
    else:
        await message.answer('Please enter a valid card number (digits only).')


@dp.message(F.text == '❌ Clear Basket')
async def clear_busket(message: types.Message):
    grocery_basket.clear()
    await message.answer('Your basket is clear', reply_markup=main_menu)


@dp.message(F.text == '⬅️ Back')
async def double_back(message: types.Message):
    await message.answer(reply_markup=main_menu)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
