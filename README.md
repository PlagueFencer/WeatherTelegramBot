# Weather Telegram Bot
It is just a simple Telegram bot that displays information about the weather in the place that was reported in the message. 

## How to use
1. You need to create your own Telegram bot in BotFather. Search @BotFather in the Telegram app and click on the result to start a conversation
2. In the conversation with BotFather, select the “New Bot” option to start creating your new bot. BotFather will guide you through the rest of the process.
3. Next, BotFather will ask you to provide a name for your bot. Choose a name that you want
4. Pick a username that you want
5. Now, you need to clone my repository. Open your terminal (Linux terminal/konsole/console, or Windows command prompt/PowerShell), now, using the `cd` command you need to select a directory, where you want to place your bot, and after this print `git clone https://github.com/PlagueFencer/WeatherTelegramBot.git` or `git clone git@github.com:PlagueFencer/WeatherTelegramBot.git`
6. Now, copy your bot token and place it in line 10 in the bot's source code (Whatever language version you want) = `telebot.TeleBot("YOUR TOKEN")`
7. Install Python on your computer if you don't have it (If you're using Debian or Debian-based distros like Ubuntu and Mint — open the terminal, print `sudo apt update` and after this print `sudo apt install python`, if you use Ubuntu use `apt-get` instead of `apt`. If your distro is Arch or Arch-based — use `sudo pacman -S python`. If it's openSUSE — use `sudo zypper install python`. If you are using another Linux distro, use your distro package manager to install Python. If your OS is Windows — ~~Install Arch Linux and install it through pacman~~ Just install Python from the official website https://www.python.org/). If you already have installed Python on your computer — good, just skip it.
8. Ok. Now you can run a code and host a bot on your computer or dedicated server — `python3 "WeatherBotLang.py"`
9. Now, open a conversation with your Bot, and just type any city name intel about what you want. 

