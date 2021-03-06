# CSB_Meet_Automation
Bot for joining online classes at the right time (This bot is optimized for S4 CSB students -  JECC).

## Refer this video for a more detailed explanation of using this bot.
[YouTube Video - Click Here](https://youtu.be/mx6fBHsQoXk)

# Usage 
The bot asks you for a ```AuthUser count``` while running. The required AuthUser count is the the position of logged in jecc mail id.The first id is 0 the second one is 1 and so on. For Eg:


![brave_R357OB31xG](https://user-images.githubusercontent.com/84261649/119509337-2e9d5280-bd8e-11eb-94c4-e5fe486e3899.png)


Here my required AuthUser count is 1 as my JECC mail id is logged in as the second account.

> The bot uses keyboard hot keys to turn off the cam and mic and also to join class.So kindly avoid engaging with the meet window while joining a class is in progress.


# Installation

## Windows 

Download the [meetautomation.exe](https://github.com/Pranavk-official/CSB_Meet_Automation/releases/download/v1.0/meetautomation.exe) from the releases and run/execute the file.


## Linux or Compiling Python Code

Download the [CsbMeetBot.zip](https://github.com/Pranavk-official/CSB_Meet_Automation/archive/refs/tags/v1.0.zip) file from the releases and extract it's contents.
The script depends or certain packages. You can install them by
```
pip3 install pyautogui
pip3 install datetime
```
or
```
pip3 install -r requirements.txt
```
After installing the dependencies you can run the script by
```
python meetautomation.py
```
or
```
python3 meetautomation.py
```
> Python3 is preffered over other versions of python.

> For the current meet bot version chromium based browers (Google,Brave) are preffered over other browsers.

Do raise an issue for feature request or bug fixes :)
