from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
import os, jdatetime
from apscheduler.schedulers.background import BackgroundScheduler
from os.path import join, getsize
from time import time, sleep
from datetime import datetime, timedelta

bot = Client(
    name="self-bot",
    api_id=11223344,
    api_hash="abcdefghijklmnopqrstuvwxyz",
    #proxy={"scheme":"socks5", "hostname":"127.0.0.1", "port":1080},
    hide_password=True
)

@bot.on_message(filters.me & filters.command(["r"]))
def raw(Client, Message):
    Message.delete()
    if len(str(Message)) <= 4090:
        bot.send_message("me", str(Message))
    elif len(str(Message)) > 4090:
        bot.send_message("me", str(Message)[0:4090])
        bot.send_message("me", str(Message)[4089:])

@bot.on_message(filters.me & filters.command(["uid"]))
def user_id(Client, Message):
    if len(Message.command) == 2:
        try:
            if str(Message.entities[1].type) == 'MessageEntityType.TEXT_MENTION':
                Message.edit_text(f'{Message.text}\n{Message.entities[1].user.id}')
            elif str(Message.entities[1].type) == 'MessageEntityType.MENTION':
                Message.edit_text(f'{Message.text}\n{bot.get_users(str(Message.command[1])).id}')
        except Exception as e:
            print(Message)
            #print("Error. Report it to the maintainer")
    elif hasattr(Message, 'reply_to_message'):
        if hasattr(Message.reply_to_message, 'from_user'):
            Message.edit(f'{Message.text}\n{str(Message.reply_to_message.from_user.id)}')

@bot.on_message(filters.me & filters.command(["info"]))
def info(Client, Message):
    try:
        Message.edit_text(f"""Firstname : {Message.reply_to_message.from_user.first_name}
Last name : {Message.reply_to_message.from_user.last_name}
Username : {Message.reply_to_message.from_user.username}
user id : {Message.reply_to_message.from_user.id}
online status : {Message.reply_to_message.from_user.status}
bot : {Message.reply_to_message.from_user.is_bot}
scam : {Message.reply_to_message.from_user.is_scam}""")
    except:
        Message.edit_text("The replied message is either removed or you forgot to reply .")

@bot.on_message(filters.me & filters.command(["idpv"]))
def idpv(Client, Message):
    try:
        try:
            Message.delete()
            bot.send_message("me",f"user id : {Message.reply_to_message.from_user.id}")
        except:
            bot.send_message("me",f"You either replied on a channel or a didn\'t even reply to any message'\nuser id : {Message.chat.id}")
    except:
        print("error")

@bot.on_message(filters.me & filters.command(["time"]))
def time(Client, Message):
    now = jdatetime.datetime.now()
    Message.edit_text(f'Time: {now.strftime("%Y-%m-%d %H:%M:%S")}')

@bot.on_message(filters.me & filters.command(["gstat"]))
def group_stat(Client, Message):
    if str(Message.chat.type) == 'ChatType.SUPERGROUP' or str(Message.chat.type) == 'ChatType.group':
        pers = [str(Message.chat.permissions.can_send_messages),str(Message.chat.permissions.can_send_media_messages),		  str(Message.chat.permissions.can_send_other_messages),str(Message.chat.permissions.can_send_polls),str(Message.chat.permissions.can_add_web_page_previews),str(Message.chat.permissions.can_change_info),str(Message.chat.permissions.can_invite_users),str(Message.chat.permissions.can_pin_messages)]
        Message.edit(f"""{Message.text}\nGroup name : {Message.chat.title}
Group type : {Message.chat.type}
Group id : {Message.chat.id}

Group permissions :
    Sending messages: {pers[0]}
    Sending media: {pers[1]}
    Sending other messages: {pers[2]}
    Sending polls: {pers[3]}
    Web previews: {pers[4]}
    Changing group info: {pers[5]}
    Inviting users: {pers[6]}
    Pin message: {pers[7]}""")

@bot.on_message(filters.me & filters.command(["dl"]))
def name(Client, Message):
    bot.delete_messages(Message.chat.id, Message.id)
    try:
        bot.download_media(Message.reply_to_message.photo.file_id)
        try:
            for root, dirs, files in os.walk('./downloads'):
                for i in files:
                    bot.send_photo("me", './downloads/' + i)
                    os.remove('./downloads/' +  i)
        except:
            pass
    except:
        bot.send_message("me", "Error occured whem downloading/uploading/removing image")

@bot.on_message(filters.me & filters.command(["udel"]))
def user_del(Client, Message):
    bot.delete_messages(Message.chat.id, Message.id)
    if str(Message.chat.type) == 'ChatType.SUPERGROUP':
        if bool(Message.reply_to_message) == True:
            if 1 == len(Message.command):
                try:
                    bot.delete_user_history(Message.chat.id, int(Message.reply_to_message.from_user.id))
                except Exception as e:
                    print(e)
                    print('\n\n')
                except:
                    bot.send_message("me", "Error occured")
        elif 2 == len(Message.command):
            print('started\n')
            try:
                bot.delete_user_history(Message.chat.id, int(Message.command[1]))
            except Exception as e:
                print(e)
                print('\n\n')
            except:
                bot.send_message("me", "Error occured")
    elif str(Message.chat.type) == 'ChatType.GROUP':
        if bool(Message.reply_to_message) == True:
            if 1 == len(Message.command):
                try:
                    print(Message.reply_to_message.from_user.id)
                    for message in bot.search_messages(Message.chat.id, int(Message.reply_to_message.from_user.id)):
                        bot.delete_messages(Message.chat.id, message.id)
                except Exception as e:
                    print(e)
                    print('\n\n')
                except:
                    bot.send_message("me", "Error occured")
            elif 2 == len(Message.command):
                try:
                    for message in bot.search_messages(Message.chat.id, int(Message.command[1])):
                        bot.delete_messages(Message.chat.id, message.id)
                except Exception as e:
                    print(e)
                    print('\n\n')
                except:
                    bot.send_message("me", "Error occured")

@bot.on_message(filters.me & filters.command(["gem"]))
def gem(Client, Message):
    bot.delete_messages(Message.chat.id, Message.id)
    bot.send_message(-1001567296645, Message.chat.title)

    for member in bot.get_chat_members(Message.chat.id):
        fo = bot.get_chat_member(Message.chat.id, member.user.id)
        chat_info = eval(str(fo).replace('false', 'False').replace('true', 'True'))
        #print(chat_info["joined_date"])
        bot.send_message(-1001567296645, f"""First name : {member.user.first_name}
Last name : {member.user.last_name}
username : {member.user.username}
user id : {member.user.id}
status : {member.status}
bot : {member.user.is_bot}
scam : {member.user.is_scam}
Join date: {chat_info.get("joined_date")}""")

@bot.on_message(filters.me & filters.command(["cg"]))
def create_grp(Client, Message):
    if 2 <= len(Message.command):
        if 3 <= len(Message.command):
            bot.create_supergroup(Message.command[1], Message.command[2])
        else:
            bot.create_supergroup(Message.command[1])
        bot.edit_message_text(Message.chat.id, Message.id, f'{Message.command[1]} group created successfully !')
    else:
        return false

@bot.on_message(filters.me & filters.command(["del"]))
def delete_msg(Client, Message):
	delndx = int(Message.command[1])+1
	i = []
	cnt = 1
	for message in bot.get_chat_history(chat_id = Message.chat.id, limit = delndx):
		#i.append(message.id)
		if len(i) == 1:
			pass
		if cnt == 200:
			bot.delete_messages(Message.chat.id, i)
			i = []
			sleep(1)
		else:
			if delndx <= 101:
				i.append(message.id)
			else:
				i.append(message.id)
	if len(i) != 0:
		bot.delete_messages(Message.chat.id, i)
		i = []
	bot.send_message(Message.chat.id,f"Deleted {delndx} messages")

@bot.on_message(filters.me & filters.command(["clean"]))
def full_cleanup(Client, Message):
    if str(Message.chat.type) != "ChatType.SUPERGROUP":
        bot.send_message(Message.chat.id, "You can only execute this command in Supergroups.")
        pass
    else:
        for message in bot.get_chat_history(chat_id=Message.chat.id):
            bot.delete_user_history(Message.chat.id, message.from_user.id)

@bot.on_message(filters.me & filters.command(["mute"]))
def mute(Client, Message):
    if (1 == len(Message.command)) & hasattr(Message, 'reply_to_message'):
        if hasattr(Message.reply_to_message, 'from_user'):
            bot.restrict_chat_member(Message.chat.id, Message.reply_to_message.from_user.id, ChatPermissions(can_send_messages = False))
    elif (2 == len(Message.command)) & hasattr(Message, 'entities'):
        if len(Message.entities) == 2:
            if str(Message.entities[1].type) == 'MessageEntityType.TEXT_MENTION':
                try:
                    bot.restrict_chat_member(Message.chat.id, Message.reply_to_message.from_user.id, ChatPermissions(can_send_messages = False))
                except:
                    Message.edit_text('Error occured muting user.\nError code: 01')
            else:
                try:
                    bot.restrict_chat_member(Message.chat.id, user_id, ChatPermissions(), datetime.now() + timedelta(minutes = Message.command[1]))
                except:
                    Message.edit_text('Error occured muting user.\nError code: 02')

@bot.on_message(filters.me & filters.command(["unmute"]))
def unmute(Client, Message):
    if (1 == len(Message.command)) & hasattr(Message, 'reply_to_message'):
        if hasattr(Message.reply_to_message, 'from_user'):
            bot.restrict_chat_member(Message.chat.id, Message.reply_to_message.from_user.id, ChatPermissions(can_send_messages = True))
    elif 2 == len(Message.command):
        try:
            bot.restrict_chat_member(Message.chat.id, Message.command[1], ChatPermissions(can_send_messages = True))
            Message.edit_text(f'{Message.text} unmuted')
        except:
            Message.edit_text(f'{Message.text}\nError occured unmuting user.\nError code: 03')

@bot.on_message(filters.me & filters.command(["ban"]))
def ban(Client, Message):
    if (1 == len(Message.command)) & hasattr(Message, 'reply_to_message'):
        if hasattr(Message.reply_to_message, 'from_user'):
            bot.ban_chat_member(Message.chat.id, Message.reply_to_message.from_user.id)
    elif (2 == len(Message.command)) & hasattr(Message, 'entities'):
        if len(Message.entities) == 2:
            if str(Message.entities[1].type) == 'MessageEntityType.TEXT_MENTION':
                try:
                    bot.ban_chat_member(Message.chat.id, Message.reply_to_message.from_user.id)
                except:
                    Message.edit_text('Error occured banning user.\nError code: 03')
            else:
                try:
                    bot.ban_chat_member(Message.chat.id, user_id, datetime.now() + timedelta(days = int(Message.command[1])))
                except:
                    Message.edit_text('Error occured banning user.\nError code: 04')

@bot.on_message(filters.me & filters.command(["unban"]))
def unban(Client, Message):
    if (1 == len(Message.command)) & hasattr(Message, 'reply_to_message'):
        if hasattr(Message.reply_to_message, 'from_user'):
            bot.unban_chat_member(Message.chat.id, Message.reply_to_message.from_user.id)
    elif (2 == len(Message.command)) & hasattr(Message, 'entities'):
        if len(Message.entities) == 2:
            if str(Message.entities[1].type) == 'MessageEntityType.TEXT_MENTION':
                try:
                    bot.unban_chat_member(Message.chat.id, Message.reply_to_message.from_user.id)
                except:
                    Message.edit_text('Error occured banning user.\nError code: 03')
            else:
                try:
                    bot.unban_chat_member(Message.chat.id, Message.command[1])
                except:
                    Message.edit_text('Error occured banning user.\nError code: 04')
    bot.unban_chat_member(Message.chat.id, Message.command[1])

@bot.on_message(filters.me & filters.command(["boom"]))
def boom(Client, Message):
    list_boom = ["🧨🌲🌲🌲🌲🌲🌲🌲🚜","🧨🌲🌲🌲🌲🌲🌲🚜","🧨🌲🌲🌲🌲🌲🚜","🧨🌲🌲🌲🌲🚜","🧨🌲🌲🌲🚜","🧨🌲🌲🚜","🧨🌲🚜","🧨🚜","💥вσσσм💥"]
    for i in list_boom:
        Message.edit(i)


bot.run()
