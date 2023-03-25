import logging, kb, time, pytube
import os
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
from downloader import second, hd1080, hd360, hd720, highest, norm, get_audio

logging.basicConfig(level=logging.INFO)
bot = Bot(token='6154632089:AAHXXUYinw6FIGzKi08heB_HvHeMkJsdrA8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cms_start(message: Message):
    await message.answer('Salom, youtube link yuboring')


@dp.message_handler()
async def down(message: Message):
    if message.text.startswith == 'https://youtube.com' or 'https://youtu.be/' and 'https://www.youtube.com/':
        try:
            global url, channel
            url = message.text
            channel = 'https://youtu.be/' + pytube.YouTube(url).video_id
            title = '📹' + pytube.YouTube(url).title + f'🔗\n{channel}\nMarhamat videoning kerakli sifatlisini tanlang👇🏻'
            thumb = pytube.YouTube(url).thumbnail_url
            await message.answer_photo(thumb, caption=title, reply_markup=kb.get_keyboard())
        except:
            await message.answer('❌ Xatolik, video manzilini tekshiring yoki botni qaytadan ishga tushuring: /start')
    else:
        await message.answer('🤖 Bot faqat youtubedan media yuklay oladi!!!')

@dp.callback_query_handler(text_contains="low")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    await call.message.delete()
    await call.message.answer('1 daqiqagacha kuting...')
    cit = call.message.chat.id
    titles = '📹' + pytube.YouTube(url).title + f'\n🔗{channel}\nVideo yuklab olindi⚡️'
    filename = pytube.YouTube(url).streams.get_by_itag(hd360).default_filename
    time.sleep(25)
    second(url)
    with open(f'./{filename}', 'rb') as video_file:
        await bot.send_video(chat_id=cit, video=video_file, caption=titles)
    os.remove(filename)

@dp.callback_query_handler(text_contains="medium")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    await call.message.delete()
    await call.message.answer('1 daqiqagacha kuting...')
    cit = call.message.chat.id
    titles = '📹' + pytube.YouTube(url).title + f'\n🔗{channel}\nVideo yuklab olindi⚡️'
    filename = pytube.YouTube(url).streams.get_by_itag(hd720).default_filename
    time.sleep(25)
    norm(url)
    with open(f'./{filename}', 'rb') as video_file:
        await bot.send_video(chat_id=cit, video=video_file, caption=titles)
    os.remove(filename)

@dp.callback_query_handler(text_contains="high")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    await call.message.delete()
    await call.message.answer('1 daqiqagacha kuting...')
    cit = call.message.chat.id
    titles = '📹' + pytube.YouTube(url).title + f'\n🔗{channel}\nVideo yuklab olindi⚡️'
    filename = pytube.YouTube(url).streams.get_by_itag(hd1080).default_filename
    time.sleep(25)
    highest(url)
    with open(f'./{filename}', 'rb') as video_file:
        await bot.send_video(chat_id=cit, video=video_file, caption=titles)
    os.remove(filename)

@dp.callback_query_handler(text_contains="mus")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    await call.message.delete()
    await call.message.answer('1 daqiqagacha kuting...')
    cit = call.message.chat.id
    titles = '📹' + pytube.YouTube(url).title + f'\n🔗{channel}\nAudio yuklab olindi⚡️'
    filename = pytube.YouTube(url).streams.get_by_itag(hd1080).default_filename
    endfilename = filename[:-4] + '.mp3'
    time.sleep(25)
    get_audio(url)
    with open(f'./{endfilename}', 'rb') as video_file:
        await bot.send_document(chat_id=cit, document=video_file, caption=titles)
    os.remove(endfilename)
    os.remove(filename)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
