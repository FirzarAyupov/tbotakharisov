from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton

# for menu
button = KeyboardButton('/menu')
orientation = InlineKeyboardButton('Расписание', callback_data='orientation')
fast = InlineKeyboardButton('Столовая', callback_data='fast')
help_text = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_text.add(button)

# for how_class
class5 = InlineKeyboardButton('𝟝', callback_data='5')
class6 = InlineKeyboardButton('𝟞', callback_data='6')
class7 = InlineKeyboardButton('𝟟', callback_data='7')
class8 = InlineKeyboardButton('𝟠', callback_data='8')
class9 = InlineKeyboardButton('𝟡', callback_data='9')
class10 = InlineKeyboardButton('𝟙𝟘', callback_data='10')
class11 = InlineKeyboardButton('𝟙𝟙', callback_data='11')

# for how_letter
letter_a = InlineKeyboardButton('а', callback_data='a')
letter_b = InlineKeyboardButton('б', callback_data='b')

# for fast_orientation InlineKeyboardMarkup.
breakfast = InlineKeyboardButton('Завтрак', callback_data='breakfast')
lunch = InlineKeyboardButton('Обед', callback_data='lunch')
afternoon_tea = InlineKeyboardButton('Полдник', callback_data='afternoon_tea')
dinner = InlineKeyboardButton('Ужин', callback_data='dinner')
sonnik = InlineKeyboardButton('Сонник', callback_data='sonnik')

orientation1 = InlineKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True).add(orientation,
                                                                fast)
fast_orientation = InlineKeyboardMarkup(one_time_keyboard=True).add(breakfast,
                                                                    lunch,
                                                                    afternoon_tea).add(
    dinner, sonnik)

how_class = InlineKeyboardMarkup(one_time_keyboard=True).add(class5, class6,
                                                             class7, class8,
                                                             class9,
                                                             class10, class11)

how_letter = InlineKeyboardMarkup(one_time_keyboard=True).add(letter_a,
                                                              letter_b)
