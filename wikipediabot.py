from aiogram import Dispatcher, Bot, types, executor
import wikipedia
API_TOKIN='5736574870:AAEvV1ceO-ZJCdt_JZuwJFDI9SPYnZ7SoH0'
bot=Bot(API_TOKIN)
dp=Dispatcher(bot)
wikipedia.set_lang('uz')
HELP_COMONDER="""
<b>/start</b>
<b>/help</b>
"""
"""
wikipedia bot kod
"""
@dp.message_handler(commands=['start'])
async def start_message(message:types.Message):
    await message.reply('<b>Botga xush kelibsiz<b>'+message.from_user.full_name)
@dp.message_handler()
async def send_wiki(message:types.Message):
    try:
      respond=wikipedia.summary(message.text)
      await message.answer(respond)
    except:
        await message.answer("Afsuski bu haqida malumot yo'q")

if __name__=='__main__':
    executor.start_polling(dp)