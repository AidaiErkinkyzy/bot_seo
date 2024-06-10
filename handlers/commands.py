from aiogram import Router,F
from aiogram.filters import Command,CommandStart
from aiogram.types import Message,CallbackQuery,FSInputFile
import handlers.keyboards as KB

router = Router()

@router.message(CommandStart())
async def start(message:Message):
    await message.answer("Hello I`m bot ceo helper",reply_markup=KB.kb)

@router.message(Command(commands=['help']))
async def help(message:Message):
    await message.answer("For help call 911")


@router.message(F.text == 'Departments')
async def departments(message:Message):
    await message.answer("Choice department",reply_markup= await KB.departments_kb())

@router.callback_query(F.data.startswith("department_"))
async def department(callback:CallbackQuery):
    department_id = callback.data.split("_")[1]
    await callback.message.answer("Люди работающие в этом отделе", reply_markup=await KB.rab_kb(department_id))

# @router.message(Command(commands=["about"]))
# async def about_us(message:Message):
#     await message.answer("We are a not a company, we are naemniki")

# @router.message(F.text.lower() == "Hello")
# async def hello(message:Message):
#     await message.answer("Hello, i am Bot Seo helper")


# reply=answer