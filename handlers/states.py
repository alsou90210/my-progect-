from aiogram.dispatcher.filters.state import State,StatesGroup 
from aiogram.dispatcher import FSMContext 
from aiogram.types import Message, Contact, ReplyKeyboardMarkup,KeyboardButton
from aiogram import types 
from bot import bot,dp 
from database.db_file import Database 
from keyboards.kb import get_keyboard 


class Registration:
    def __init__(self,message: Message):
        self.message = message


    async def registration_users(self,message: Message):
        class RegistrationState(StatesGroup):
            phone = State()


        await RegistrationState.phone.set ()
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        keyboard.add(KeyboardButton ('Отправить номер телефона',request_contact=True))
        await message.answer('Пожалуйста отправьте нам  свой номер телефона для регистрации ',reply_markup=keyboard)


        @dp.message_handler(content_types=types.ContentType.CONTACT,state=RegistrationState.phone )
        async def phone_state(message: Message,state:FSMContext):
            async with state.proxy() as data:
                data ['phone'] = message.contact.phone_number
                phone =data ['phone']
                await message.answer('Привет ты зарегистрирован', reply_markup=get_keyboard('start_menu'))


                db = Database()
                db.connect()
                db.create_user_table()
                user_id = message.from_user.id
                first_name = message.from_user.first_name
                db.add_user(first_name,user_id,phone)   
                dp.closed()


            await state.finish()