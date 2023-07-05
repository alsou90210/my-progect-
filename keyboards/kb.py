from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


def get_keyboard(name:str):
    if name == 'start_menu':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('Товары'),('Корзина'))
        keyboard.add(KeyboardButton('Личный кабинет'),('Тех.Поддержка'))
        

    elif name == 'test':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('test'),('test2'))   


    return keyboard    