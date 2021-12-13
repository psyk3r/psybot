# PSYBOT
>Telegram self cli bot


## How to install
Before installing from the requirements file, make sure that gcc and clang are installed in your device.
```bash
pip3 install -r requirements.txt
```
#### After installing the requirements, you have to make some changes to your **config.ini** file:
##### 1- Replace your api id and api hash with the defaults in the file
##### 2- Set your SOCKS5 proxy settings if you have any (Or you can just use tor)<br>


## How to run
```bash
python3 self.py
```

#### Commands
###### /uid (Shows the user id of the replied message in current chat)
###### /aid (Sends the user id,name,lastname,username,online status,is bot,is scam to aid database)
###### /idpv (Sends the user id of the replied message in your Saved Messages)
###### /info (Sends the user id,name,lastname,username,online status,is bot,is scam in current chat)
###### /time (Shows time(in Solar date format))
###### /stat (Send the replied user's online status)
###### /gstat (Shows current group permission)
###### /dl (Saves the replied photo (can download destructible photos too))
###### /r (Sends all of the parameters of a message sent in saved messages)
###### /ban (bans a user from group. eg:/ban user_id or reply to the user and just type /ban)
###### /pin (Pins a message)
###### /unpin (Unpins a message)
###### /del (Deletes a selected amount of messages. eg: /del 10)
###### /ldel (Deletes all of your sent messages in a group)
###### /lock (Locks a group and normal members can't send messages)
###### /unlock (Unlocks the group)
###### /clone (Creates a new Group and clones all the messages in it(user may face limitations in cloning because the amount of the messages))
###### /db num (Sends the replied user's id,name,lastname,username,online status,is bot,is scam,Message in your database. eg: /db 1)
###### /s (Searches for a key word given by the user and returns the matched cases in links. eg: /s john)
###### /gem (Sends the information of all group members. Including : user id,name,lastname,username,online status,is bot,is scam,join date)
