from aiogram.types import ReplyKeyboardMarkup
from keyboards.buttons import cl_btn_job, cl_btn_loc, cl_btn_menu
from keyboards.buttons import adm_btn_load, adm_btn_delete

client_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
client_keyboard.row(cl_btn_job, cl_btn_loc, cl_btn_menu)
# client_keyboard.row(contact_button, location_button)

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyboard.row(adm_btn_load, adm_btn_delete)
