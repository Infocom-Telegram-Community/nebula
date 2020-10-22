<p align="center">
<img src="https://i.imgur.com/Qsdgosd.jpg" alt="Smiley face" height="500" width="500">
</p>

[![Group](https://img.shields.io/badge/Group-SquirrelNetwork-blue)](https://t.me/squirrelnetwork)

[![Python3.7+](https://img.shields.io/badge/Python-3.7%2B-green.svg)](https://www.python.org/downloads)
[![Squirrel-Network](https://circleci.com/gh/Squirrel-Network/nebula.svg?style=shield)](https://app.circleci.com/pipelines/github/Squirrel-Network/nebula)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4988792a122f410bb6ef1bbca6c3d6ad)](https://www.codacy.com/gh/Squirrel-Network/nebula?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Infocom-Telegram-Community/nebula&amp;utm_campaign=Badge_Grade)

---

# This bot is no longer maintained, patches are made from time to time. The new bot is developed here: https://github.com/Squirrel-Network/nebula8

## How to start

<b>Clone this repo:</b> ```git clone https://github.com/Squirrel-Network/nebula.git```
<br>
<b>Import the database from the /SQL folder in your database(MariaDB)</b>
<br>
<b>In your shell start this bot use this command=></b> ```python3 bot.py```
<br>
<br>

## Requirements ⚙️

Besides [Python 3.7+](https://www.python.org/downloads/) we will be using the following packages:

<b>Install requirements</b> (https://github.com/Squirrel-Network/nebula/blob/master/requirements.txt)
<br>
<b>Command:</b> ```pip install -r requirements.txt``` <b>Or</b> ```pip3 install -r requirements.txt```

### Do you have problems installing mysqlclient requirements?
Use this command:
<ul>
<li><b>Centos:</b> sudo yum install mysql-devel</li>
<li><b>Ubuntu/Debian:</b> sudo apt-get install python-dev default-libmysqlclient-dev</li>
<li><b>Fedora:</b> sudo dnf install python python-devel mysql-devel redhat-rpm-config gcc</li>
</ul>

<br>

## Global Commands List
<br>
<h3>Commands to be executed in response to a username</h3>
<br>


| Command | Description |
| --- | --- |
| /ban -m {text} or /ban @username -m {text} | Ban the user |
| /unban | Unban the user |
| /mute | mute user |
| /unmute | unmute user |
| /info | user information and chat id |
| /delete | delete message |
| /kick | kick user |
<br>
<h3>Commands to be executed in chat</h3>
{text} = text to insert

| Command | Description |
| --- | --- |
| /a {text}| announcement |
| /setpin {text} | set pin message by bot |
| /pin | pin message by bot |
| /info | user information and chat id |
| /delete | delete message |
| /kick | kick user |
| /warn | warn user(experimental function) |
| /unwarn | unwarn user(experimental function) |
| /weather yourcityname | weather |
| /staff | List group staff |
| /silence | Mute the whole group |
| /say {text}  | Get the bot talking |
| /badword {text} | Add badword in your group |
| /badlist  | Badword List |
<br>
<h3>Welcome Settings</h3>

| Command | Description |
| --- | --- |
| /setwelcome | set the welcome for your group |
| /listwelcome | watch your welcome by group |
| /updatewelcome | update your welcome by group |
| /add BUTTON,example.com | add button into welcome |
| /listbutton | remove and see the welcome buttons |

<br>
<h3>Voting System Settings</h3>

| Command | Description |
| --- | --- |
| /enable | enables voting for a user in the group |
| /vote or /downvote | Vote for a user or Remove a user's vote |
| /score | View your score in the group |


<br>

### Do you want to use Docker? 🐳
Go to: https://github.com/Squirrel-Network/nebula/tree/master/docker

<b>Important Note: This bot only works with python telegram bot 12.1.1+</b>
<br>

## How can I create a plugin?
🔷 Go to the /plugins folder (https://github.com/Squirrel-Network/nebula/tree/master/plugins)
<br>
🔷 inside the plugins folder you will find the ```__init__.py``` file
    Every time you add a plugin inside the folder you have to add the name of the file in the ```__all__``` array
    For example:
    if we create the banana.py file we have to insert banana inside ```__all__```
    <br>
    <a href="https://imgur.com/pMiwxIR"><img src="https://i.imgur.com/pMiwxIR.png" title="source: imgur.com" /></a>
    <a href="https://imgur.com/dR0nN1P"><img src="https://i.imgur.com/dR0nN1P.png" title="source: imgur.com" /></a>
    <br>
🔷Now let's go to bot.py and enter our plugin command with the following command line:
<br>
    ```FUNCTION(CMH("banana", plugins.banana.init))```
    where we will insert plugins.filename.functionname
    and in "banana" enter the command that will work on telegram (/banana)
    <br>
    <a href="https://imgur.com/sOoPruP"><img src="https://i.imgur.com/sOoPruP.png" title="source: imgur.com" /></a>
    <br>
🔷 Video Tutorial: https://youtu.be/Bmm37wG1EZQ

# Credits
<br>
Thanks to https://github.com/SteelManITA
<br>
Thanks to https://github.com/stefano-mecocci
<br>
Thanks to https://github.com/JervNorsk
<br>
Thanks to https://github.com/PaulSonOfLars/tgbot

## License 📄

Please read the [LICENSE](LICENSE) provided in this rep
