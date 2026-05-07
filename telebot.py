import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    FSInputFile,
)
# 1algaritim nima va u nima ish qiladi, nima yaratish mumkin imtihonni 100% tugatib kelish 


API_TOKEN = "8711283606:AAH1vmRwZhJ4K3cjvEE_qhfcRnskNk-TGbE"





logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))




def get_main_menu():
    buttons = [
        [
            InlineKeyboardButton(
                text="🇺🇿 O'zbekiston viloyatlari", callback_data="menu_regions"
            )
        ],
        [
            InlineKeyboardButton(
                text=" Dunyo davlatlari", callback_data="menu_countries"
            )
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_regions_menu():
    buttons = [
        [
            InlineKeyboardButton(text="Andijon", callback_data="reg_andijon"),
            InlineKeyboardButton(text="Buxoro", callback_data="reg_buxoro"),
            InlineKeyboardButton(text="Farg'ona", callback_data="reg_fargona"),
        ],
        [
            InlineKeyboardButton(text="Jizzax", callback_data="reg_jizzax"),
            InlineKeyboardButton(text="Xorazm", callback_data="reg_xorazm"),
            InlineKeyboardButton(text="Namangan", callback_data="reg_namangan"),
        ],
        [
            InlineKeyboardButton(text="Navoiy", callback_data="reg_navoiy"),
            InlineKeyboardButton(text="Qashqadaryo", callback_data="reg_qashqadaryo"),
            InlineKeyboardButton(text="Samarqand", callback_data="reg_samarqand"),
        ],
        [
            InlineKeyboardButton(text="Sirdaryo", callback_data="reg_sirdaryo"),
            InlineKeyboardButton(text="Surxondaryo", callback_data="reg_surxondaryo"),
            InlineKeyboardButton(text="Toshkent v.", callback_data="reg_toshkent"),
        ],
        [InlineKeyboardButton(text=" Orqaga", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_countries_menu():
    buttons = [
        [
            InlineKeyboardButton(text="🇺🇸 AQSH", callback_data="cnt_usa"),
            InlineKeyboardButton(text="🇷🇺 Rossiya", callback_data="cnt_russia"),
            InlineKeyboardButton(text="🇹🇷 Turkiya", callback_data="cnt_turkey"),
        ],
        [
            InlineKeyboardButton(text="🇰🇷 Koreya", callback_data="cnt_korea"),
            InlineKeyboardButton(text="🇦🇪 BAA", callback_data="cnt_uae"),
            InlineKeyboardButton(text="🇨🇳 Xitoy", callback_data="cnt_china"),
        ],
        [InlineKeyboardButton(text=" Orqaga", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)




@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Xush kelibsiz! Kerakli bo'limni tanlang:", reply_markup=get_main_menu()
    )


@dp.callback_query(F.data == "back_to_main")
async def back_handler(callback: types.CallbackQuery):
    await callback.message.edit_text("Bo'limni tanlang:", reply_markup=get_main_menu())


@dp.callback_query(F.data == "menu_regions")
async def show_regions(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "O'zbekiston viloyatlarini tanlang:", reply_markup=get_regions_menu()
    )


@dp.callback_query(F.data == "menu_countries")
async def show_countries(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Dunyo davlatlarini tanlang:", reply_markup=get_countries_menu()
    )


@dp.callback_query(F.data.startswith("reg_") | F.data.startswith("cnt_"))
async def send_video_handler(callback: types.CallbackQuery):
    data = callback.data
    video_file_name = ""
    caption_text = ""

    if data.startswith("reg_"):
        region = data.split("_")[1]
        regions_dict = {
            "andijon": ("andijon.mp4", "🇺🇿 Andijon viloyati!"),
            "buxoro": ("buxoro.mp4", "🇺🇿 Ko'hna Buxoro!"),
            "fargona": ("farg'ona.mp4", "🇺🇿 Farg'ona vodiysi!"),
            "jizzax": ("jizzah.mp4", "🇺🇿 Jizzax tabiati!"),
            "xorazm": ("xorazim.mp4", "🇺🇿 Xiva va Xorazm!"),
            "namangan": ("namangan.mp4", "🇺🇿 Gullar diyori Namangan!"),
            "navoiy": ("navoiy.mp4", "🇺🇿 Navoiy viloyati!"),
            "qashqadaryo": ("qashqadaryo.mp4", "🇺🇿 Qashqadaryo vohasi!"),
            "samarqand": ("samarqand.mp4", "🇺🇿 Boqiy Samarqand!"),
            "sirdaryo": ("sirdaryo.mp4", "🇺🇿 Sirdaryo kengliklari!"),
            "surxondaryo": ("surhondaryo.mp4", "🇺🇿 Surxondaryo tabiati!"),
            "toshkent": ("toshkent.mp4", "🇺🇿 Toshkent viloyati!"),
        }
        video_file_name, caption_text = regions_dict.get(region, ("", ""))

    elif data.startswith("cnt_"):
        country = data.split("_")[1]
        countries_dict = {
            "usa": ("usa.mp4", "🇺🇸 Amerika Qo'shma Shtatlari!"),
            "russia": ("russiya.mp4", "🇷🇺 Rossiya Federatsiyasi!"),
            "turkey": ("turkey.mp4", "🇹🇷 Turkiya davlati!"),
            "korea": ("korea.mp4", "🇰🇷 Janubiy Koreya!"),
            "uae": ("uae.mp4", "🇦🇪 Birlashgan Arab Amirliklari!"),
            "china": ("china.mp4", "🇨🇳 Xitoy Xalq Respublikasi!"),
        }
        video_file_name, caption_text = countries_dict.get(country, ("", ""))

    file_path = os.path.join(BASE_DIR, video_file_name)
    await callback.answer("Video yuklanmoqda...")

    if os.path.exists(file_path):
        try:
            video_input = FSInputFile(file_path)
            await callback.message.answer_video(video=video_input, caption=caption_text)
        except Exception as e:
            await callback.message.answer(f"Xatolik: {e}")
    else:
        await callback.message.answer(f" {video_file_name} topilmadi.")


async def main():
    # Webhookni tozalash
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot muvaffaqiyatli ishga tushdi (Proxy orqali)...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot to'xtatildi")
