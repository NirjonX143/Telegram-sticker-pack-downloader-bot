import telebot
from tgsdl import download_sticker_pack
import os

bot_token = "6294861300:AAFA11qN7tu-RssUwnNoHOmO4G9LH1qbanw"
#channel id
log_channel = int(-1001806314462) # Change id
bot = telebot.TeleBot(bot_token)
pic = "https://external-preview.redd.it/cS0icfKcdsND_SJTYlbXxklp32qZYOnawKHKS88XSsE.png?format=pjpg&auto=webp&s=24bc4881f7bbf5ba6c650023ca753afdfa397675"

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_photo(message.chat.id,photo=pic,caption= 'ꜱᴇɴᴅ ꜱᴛɪᴄᴋᴇʀ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ.')

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
	cha_id = message.chat.id
	meg_id = message.message_id
	try:
	  asg = bot.send_message(message.chat.id, text="ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ, ɪᴛ ᴡɪʟʟ ᴛᴀᴋᴇ ꜱᴏᴍᴇ ᴛɪᴍᴇ.")
	  sticker_id = message.sticker.file_id
	  sticker_set = bot.get_sticker_set(message.sticker.set_name)
	  sticker_pack_name = sticker_set.name
	  sticker_pack_url = f"https://t.me/addstickers/{sticker_pack_name}"
	  num_stickers = len(sticker_set.stickers)
	  from tgsdl import download_sticker_pack
	  download_sticker_pack(sticker_pack_url)
	  file_zip = f"Sticker/{sticker_pack_name}.zip"
	  with open(file_zip,"rb") as file:
	   bot.send_document(message.chat.id, file,caption=f"ʙᴏᴛ : [ᴛɢꜱᴛɪᴄᴋᴇʀᴅʟʙᴏᴛ](https://t.me/TgStickerDlbot)\nᴀᴅᴍɪɴ : [ʟɪʟʟɪꜱʟᴏᴠᴇ](https://t.me/Beverlillis)\nᴛᴏᴛᴀʟ ꜱᴛɪᴄᴋᴇʀ : {num_stickers}",parse_mode="Markdown")
	   #send log
	   bot.send_document(chat_bc,zip,caption=f"ʙᴏᴛ : [ᴛɢꜱᴛɪᴄᴋᴇʀᴅʟʙᴏᴛ](https://t.me/TgStickerDlbot)\nᴛʜᴀɴᴋꜱ ᴛᴏ : {first_name}\nᴛᴏᴛᴀʟ ꜱᴛɪᴄᴋᴇʀ : {num_stickers}",parse_mode="Markdown")
	   bot.delete_message(message.chat.id, asg.message_id)
	   
	  try:
	   os.remove(file_zip)
	  except:
	   pass
	except:
	  bot.send_message(chat_id, 'STICKER NOT FOUND')


bot.infinity_polling()
