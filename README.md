# PSYBOT V0.2 Pre-Alpha
>Telegram self cli bot


## How to install
Before installing from the requirements file, make sure that gcc and clang are installed in your device.
```bash
pip3 install -r requirements.txt
```
#### After installing the requirements, you have to make some changes to your **config.ini** file:
##### 1- Replace your api id and api hash with the defaults in 9th line of psybot.py
##### 2- Set your SOCKS5 proxy settings if you have any (Or you can just use tor)<br>


## How to run
```bash
python3 self.py
```

#### Commands
###### /uid (Shows the user id of a tagged tg user)
###### /idpv (Sends the user id of the replied message in your Saved Messages)
###### /info (Sends the user id,name,lastname,username,online status,is bot,is scam in current chat)
###### /time (Shows time(in Solar date format))
###### /gstat (Shows current group permission)
###### /dl (Saves the replied photo (can download destructible photos too))
###### /udel (Removes all messages sent from a specific user in a group/supergroup)
###### /clean (Removes all messages sent in a supergroup ASAP)
###### /r (Sends all of the parameters of a message sent in saved messages)
###### /ban (Bans a user from group. eg:/ban id or reply to the user and just type /ban)
###### /unban (Unbans a user from group. eg:/ban id)
###### /mute (Mutes a user in a group/supergroup)
###### /unmute (Unmutes a user in a group/supergroup)
###### /del (Deletes a selected amount of messages. eg: /del 10)
###### /gem (Sends the information of all group members. Including : user id,name,lastname,username,online status,is bot,is scam,join date)
###### /cg (Creates a supergroup)
###### /boom (Shows an explosion animation created with emojies)
###### /get_id (Enumerates a user's id using his/her username)
###### /google (Googles the entered phrase/sentence)
###### /weather (Shows weather information of the given city)

### ToDo List
- [X] Reprogram this script compatible with pyrogram v2
- [ ] Adapt psybot v0.1 features with the new release
- [ ] Debug and error handling
