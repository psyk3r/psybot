from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
import os, jdatetime
from os.path import join, getsize

bot = Client(
    session_name="new-client-bot",
    config_file="config.ini"
)

# Channel id or group id to use as database. Format: dbs = int(-1002003004005)
aid = int()
gem = int()

db0 = int()
db1 = int()
db2 = int()

if 'db0' not in locals() or 'db1' not in locals() or 'db2' not in locals():
    print('You don\'t have a database')
    exit()

elif bool(db0) == False or bool(db1) == False or bool(db2) == False:
    print('You don\'t have a database')
    exit()

@bot.on_message(filters.me & filters.command(["uid"]))
async def name(Client, Message):  
    await bot.edit_message_text(Message.chat.id,Message.message_id, f"user id : {Message.reply_to_message.from_user.id}")

@bot.on_message(filters.me & filters.command(["aid"]))
async def name(Client, Message):
    try:
        await bot.send_message(aid,f"""Firstname : {Message.reply_to_message.from_user.first_name}
Last name : {Message.reply_to_message.from_user.last_name}
Username : {Message.reply_to_message.from_user.username}
user id : {Message.reply_to_message.from_user.id}
online status : {Message.reply_to_message.from_user.status}
bot : {Message.reply_to_message.from_user.is_bot}
scam : {Message.reply_to_message.from_user.is_scam}""")
        await bot.delete_messages(Message.chat.id, Message.message_id)
    except:
        await bot.edit_message_text(Message.chat.id, Message.message_id, "The replied message is either removed or you forgot to reply .")

@bot.on_message(filters.me & filters.command(["idpv"]))
async def name(Client, Message):
    try:
        try:
            await bot.delete_messages(Message.chat.id, Message.message_id)
            await bot.send_message("me",f"user id : {Message.reply_to_message.from_user.id}")
        except:
            await bot.send_message("me",f"user id : {Message.chat.id}")
    except:
        print("error")

@bot.on_message(filters.me & filters.command(["info"]))
async def name(Client, Message):
    await bot.send_message(Message.chat.id,f"""Firstname : {Message.reply_to_message.from_user.first_name}
Last name : {Message.reply_to_message.from_user.last_name}
Username : {Message.reply_to_message.from_user.username}
user id : {Message.reply_to_message.from_user.id}
online status : {Message.reply_to_message.from_user.status}
bot : {Message.reply_to_message.from_user.is_bot}
scam : {Message.reply_to_message.from_user.is_scam}""")

@bot.on_message(filters.me & filters.command(["time"]))
async def name(Client, Message):
    now = jdatetime.datetime.now()
    await bot.edit_message_text(Message.chat.id, Message.message_id, f'Time: {now.strftime("%Y-%m-%d %H:%M:%S")}')
        

@bot.on_message(filters.me & filters.command(["stat"]))
async def name(Client, Message):
   try:
       await bot.edit_message_text(Message.chat.id,Message.message_id,f"online status : {Message.reply_to_message.from_user.status}")
   except:
        await bot.edit_message_text(Message.chat.id,Message.message_id, "The replied message is either removed or you forgot to reply .")

@bot.on_message(filters.me & filters.command(["gstat"]))
async def name(Client, Message):
    if Message.chat.type == 'supergroup' or  Message.chat.type == 'group':
        pers = [str(Message.chat.permissions.can_send_messages),str(Message.chat.permissions.can_send_media_messages),str(Message.chat.permissions.can_send_stickers),str(Message.chat.permissions.can_send_animations),str(Message.chat.permissions.can_send_games),str(Message.chat.permissions.can_use_inline_bots),str(Message.chat.permissions.can_add_web_page_previews),str(Message.chat.permissions.can_send_polls),str(Message.chat.permissions.can_change_info),str(Message.chat.permissions.can_invite_users),str(Message.chat.permissions.can_pin_messages)]
        await bot.edit_message_text(Message.chat.id, Message.message_id, f"""Group name : {Message.chat.title}
Group type : {Message.chat.type}
Group id : {Message.chat.id}

Group permissions :
    Sending messages: {pers[0]}
    Sending media: {pers[1]}
    Sending stickers: {pers[2]}
    Web previews: {pers[3]}
    Sending polls: {pers[4]}
    Changing group info: {pers[5]}
    Sending gifs or animations: {pers[6]}
    Sending games: {pers[7]}
    Using inline bots: {pers[8]}
    Inviting users: {pers[9]}
    Pin message: {pers[10]}""")

@bot.on_message(filters.me & filters.command(["dl"]))
async def name(Client, Message):
    await bot.delete_messages(Message.chat.id, Message.message_id)
    try:
        await bot.download_media(Message.reply_to_message.photo.file_id)
        try:
            for root, dirs, files in os.walk('./downloads'):
                for i in files:
                    await bot.send_photo("me", './downloads/' + i)
                    await os.remove('./downloads/' +  i)
        except:
            pass
    except:
        await bot.send_message("me", "Error occured whem downloading/uploading/removing image")

    
@bot.on_message(filters.me & filters.command(["r"]))
def name(Client, Message):
    bot.delete_messages(Message.chat.id, Message.message_id)
    mes = str(Message)
    if len(mes) <= 4096:
        bot.send_message("me", mes)
    elif len(mes) > 4096:
        bot.send_message("me", mes[0:4096])
        bot.send_message("me", mes[4096:])

@bot.on_message(filters.me & filters.command(["ban"]))
def name(Client, Message):
    if 1 >= len(Message.command):
        user = Message.reply_to_message.from_user.id
        bot.kick_chat_member(Message.chat.id,user)
        bot.send_message(Message.chat.id,"banned user")
    else:
        bot.kick_chat_member(Message.chat.id,Message.command[1])
        bot.send_message(Message.chat.id,"banned user")


@bot.on_message(filters.me & filters.command(["unban"]))
async def name(Client, Message):
    await bot.unban_chat_member(Message.chat.id,Message.command[1])
    
@bot.on_message(filters.me & filters.command(["pin"]))
async def name(Client, Message):
    await bot.pin_chat_message(Message.chat.id, Message.reply_to_message.message_id)
    
@bot.on_message(filters.me & filters.command(["unpin"]))
async def name(Client, Message):
    await bot.unpin_chat_message(Message.chat.id, Message.reply_to_message.message_id)

@bot.on_message(filters.me & filters.command(["del"]))
def name(Client, Message):
    delndx = int(Message.command[1]) + 1
    i = []
    for message in bot.iter_history(Message.chat.id, delndx):
        i.append(message.message_id)
    bot.send_message(Message.chat.id,f"Deleted {len(i)-1} messages")
    bot.delete_messages(Message.chat.id, i)

@bot.on_message(filters.me & filters.command(["ldel"]))
def name(Client, Message):
    bot.delete_messages(Message.chat.id, Message.message_id)
    if Message.chat.type == 'supergroup' or  Message.chat.type == 'group':
        delm = []
        for message in bot.search_messages(Message.chat.id, from_user="me"):
            delm.append(message.message_id)
        bot.delete_messages(Message.chat.id, delm)

@bot.on_message(filters.me & filters.command(["lock"]))
async def name(Client, Message):
    try:
        await bot.set_chat_permissions(Message.chat.id, ChatPermissions(can_send_messages=False))
        await bot.edit_message_text(Message.chat.id, Message.message_id, "locked group :)")     
    except:
        await bot.send_message(Message.chat.id, "You can't change the permissions of a dm or a channel .")

@bot.on_message(filters.me & filters.command(["unlock"]))
async def name(Client, Message):
    try:
        await bot.set_chat_permissions(Message.chat.id, ChatPermissions(can_send_messages=True))
        await bot.edit_message_text(Message.chat.id, Message.message_id, "unlocked group :)")     
    except:
        await bot.send_message(Message.chat.id, "You can't change the permissions of a dm or a channel .")

@bot.on_message(filters.me & filters.command(["clone"]))
def name(Client, Message):
    try:
        bot.delete_messages(Message.chat.id,Message.message_id)
        title = str(Message.chat.title)+" backup"
        det = bot.create_supergroup(title)
        for msg in bot.iter_history(Message.chat.id,):
            bot.copy_message(det.id,Message.chat.id,msg.message_id)
        
    except:
        bot.send_message(Message.chat.id, "You can only clone a group or a channel")
        return False
    
@bot.on_message(filters.me & filters.command(["db"]))
def name(Client, Message):
    bot.delete_messages(Message.chat.id, Message.message_id)
    try:
        if Message.command[1] == "0":
            bot.send_message(db0, f"""Firstname : {Message.reply_to_message.from_user.first_name}
Last name : {Message.reply_to_message.from_user.last_name}
Username : {Message.reply_to_message.from_user.username}
user id : {Message.reply_to_message.from_user.id}
online status : {Message.reply_to_message.from_user.status}
bot : {Message.reply_to_message.from_user.is_bot}
scam : {Message.reply_to_message.from_user.is_scam}
        """)
            bot.forward_messages(db0,Message.chat.id,Message.reply_to_message.message_id)
        
        if Message.command[1] == "1":
            bot.send_message(db1, f"""Firstname : {Message.reply_to_message.from_user.first_name}
Last name : {Message.reply_to_message.from_user.last_name}
Username : {Message.reply_to_message.from_user.username}
user id : {Message.reply_to_message.from_user.id}
online status : {Message.reply_to_message.from_user.status}
bot : {Message.reply_to_message.from_user.is_bot}
scam : {Message.reply_to_message.from_user.is_scam}
        """)
            bot.forward_messages(db1, Message.chat.id, Message.reply_to_message.message_id)
        
        if Message.command[1] == "2":
            bot.send_message(db2, f"""Firstname : {Message.reply_to_message.from_user.first_name}
Last name : {Message.reply_to_message.from_user.last_name}
Username : {Message.reply_to_message.from_user.username}
user id : {Message.reply_to_message.from_user.id}
online status : {Message.reply_to_message.from_user.status}
bot : {Message.reply_to_message.from_user.is_bot}
scam : {Message.reply_to_message.from_user.is_scam}
        """)
            bot.forward_messages(db2, Message.chat.id, Message.reply_to_message.message_id)
    except:
        bot.send_message(db0, "Error occured at saving message in database .")

@bot.on_message(filters.me & filters.command(["s"]))
def name(Client, Message):
	sqr = []
	bot.edit_message_text(Message.chat.id, Message.message_id, "Sending search result")
	for m in bot.search_messages(Message.chat.id,query=Message.command[1]):
		sci = str(m.sender_chat.id)[4:14]
		sqr.append(f"https://t.me/c/{sci}/{m.message_id}\n")
	bot.edit_message_text(Message.chat.id, Message.message_id, ", ".join(sqr).replace(', ',''))

@bot.on_message(filters.me & filters.command(["gem"]))
def name(Client, Message):
    bot.delete_messages(Message.chat.id, Message.message_id)
    bot.send_message(gem,Message.chat.title)
    
    for member in bot.iter_chat_members(Message.chat.id):
        fo =  bot.get_chat_member(Message.chat.id, member.user.id)
        chat_info = eval(str(fo).replace('false', 'False').replace('true', 'True'))
        bot.send_message(gem, f"""First name : {member.user.first_name}
Last name : {member.user.last_name}
username : {member.user.username}
user id : {member.user.id}
status : {member.status}
bot : {member.user.is_bot}
scam : {member.user.is_scam}
Join date: {chat_info.get("joined_date")}""")

        
bot.run()
