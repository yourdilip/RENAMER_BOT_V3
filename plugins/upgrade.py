"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 1231  🇮🇳/🌎 15$  per Year 
	
	**VIP 2 **
	Daily Upload limit Unlimited 
	Price Rs  2051  🇮🇳/🌎 25$  per Year
	
	
	Upi not supporte``Not allowed```
	
	Contect To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/YourDilip")], 
        			[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 1231  🇮🇳/🌎 15$  per Year 
	
	**VIP 2 **
	Daily Upload limit Unlimited
	Price Rs  2051  🇮🇳/🌎 25$  per Year
	
	
	Upi not supporte``Not allowed```
	
	Contect To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/YourDilip")], 
        			[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
