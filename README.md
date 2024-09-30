# Weather Telegram Bot
It is just a simple Telegram bot that displays information about the weather in the place that was reported in the message. 

## How to use
1. You need to create your own Telegram bot in BotFather. Search @BotFather in the Telegram app and click on the result to start a conversation
2. In the conversation with BotFather, select the “New Bot” option to start creating your new bot. BotFather will guide you through the rest of the process.
3. Next, BotFather will ask you to provide a name for your bot. Choose a name that you want
4. Pick a username that you want
5. Install **git** on your computer if you don't have it (Just use package manager of your Linux distro, or install it from official website if your OS is Windows). If you already have installed git on your computer — good, just skip it.
6. Now, you need to clone my repository. Open your terminal (Linux terminal/konsole/console, or Windows command prompt/PowerShell), now, using the `cd` command you need to select a directory, where you want to place your bot, and after this print `git clone https://github.com/PlagueFencer/WeatherTelegramBot.git` or `git clone git@github.com:PlagueFencer/WeatherTelegramBot.git`. Once installed, use the `cd WeatherTelegramBot` command in a terminal to change terminal to a bot directory. *Don't close a terminal after this.*
7. Now, copy your bot token and place it in line 10 in the bot's source code (Whatever language version you want) = `telebot.TeleBot("YOUR TOKEN")`
8. Install Python on your computer if you don't have it (Just use package manager of your Linux distro, or install it from official website if your OS is Windows). If you already have installed Python on your computer — good, just skip it.
9. Now, you need to install **telebot** and **pyowm**. Print `pip3 install telebot` or `pip install telebot` and after this print `pip3 install pyowm` or `pip install pyowm` in your terminal. *Don't close a terminal after this.*
10. Ok. Now you can run a code and host a bot on your computer or dedicated server — `python3 "WeatherBotLang.py"`
11. Now, open a conversation with your Bot, and just type any city name intel about what you want. 

P.S
Actually, I don't know if this even works. This code is 4 yo :) 
UPD:
Yes, it still works. Shit happens.
