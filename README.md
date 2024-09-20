# Weather Telegram Bot
It is just a simple Telegram bot that displays information about the weather in the place that was reported in the message. 

## How to use
1. You need to create own telegram bot in BotFather. Search @BotFather in Telegram app and click on the result to start a concersation
2. In the conversation with BotFather, select the "New Bot" option to start creating your new bot. BotFather will guide you through the rest of the process.
3. Next, BotFather will ask you to provide a name for your bot. Choose a name what you want
4. Choose a username what you want
5. Now, you need to clone my repository. Open your terminal (Linux terminal/konsole/console, or Windows command promt/PowerShell), now, using `cd` command you need to choose a directory, where you want to place your bot, and after this print `git clone https://github.com/PlagueFencer/WeatherTelegramBot.git` or `git clone git@github.com:PlagueFencer/WeatherTelegramBot.git`
6. Now, copy your bot token and place it in line 10 in bots source code (Whatever language version what you want) = `telebot.TeleBot("YOUR TOKEN")`
7. Install Python on your computer if you doesn't have it (If you using Debian or Debian-based distros like Ubuntu and Mint - open terminal, print `sudo apt update` and after this print `sudo apt install python`, if you use Ubuntu use `apt-get` istead of `apt`. If your distro is Arch or Arch-based - use `sudo pacman -S python`. If its OpenSuse - use `sudo zypper install python`. If you using some other Linux distro - just use your distro package manager to install Python. If your OS is Windows - ~~Install Arch Linux and install it throve pacman~~ Just install Python from oficial website https://www.python.org/). If you already have installed Python on your computer - good, just skip it.
8. Ok. Now you can run a code and host a bot on your computer or dedicated server. 
9. Now, open a conversation 
