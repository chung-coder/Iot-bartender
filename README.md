# IoT-bartender
![](https://i.imgur.com/jgNbMPh.png)

## Overview
This is an **AI bartender with Age verification**. Because of the working holiday in Orchid Island during the summer vacation, I want to share Original Cocktail that I met in this summer through this project.
To implement this project, I would use five drinks and rice wine. As for user, there are three steps to operate.

a.	First, user need to offer their selfie to identify age. If their age is less than 18 years old, they cannot choose rice wine as a component of drinks.

b.	Second, user need to choose the drinks what they like and the proportion what they want on their mobile device. 

c.	Third, the mobile device will generate an qr-code and user can use it to pick their drink.

![](https://i.imgur.com/cbIxT6t.png)


## Components
### Hardward
- Raspberry Pi 3 *1
- Logitech Webcam *1
- 12V Switching Power Supply *1
- Jumper wires
- breadboard
- 12V DC Dosing Pump Peristaltic *6
- Food Grade Silicone Tubing *3m
- 8 Channel DC 5V Relay Module *1
- power cable *1

### Software
- Python 3.7
- Open-Vino
- Python Telegram Bot


### Accessories
- 紅標米酒
- 雪碧
- 國農牛乳
- 伯朗咖啡
- 蔓越莓汁
- 美粒果


## Circuit Diagram
![](https://i.imgur.com/QBvCgU7.png)

Didn’t put webcam on the circuit diagram!

Just plug them in your raspberry pi. It’s simple!

## How does Iot-bartender really look like

   ![](https://i.imgur.com/W03h3U5.jpg)
   
   ![](https://i.imgur.com/Ry2dcOi.jpg)

## Telegram Bot UI設計
![](https://i.imgur.com/i0inCYF.png)

## System Diagram on this project

![](https://i.imgur.com/KXtfexU.png)

## [Click here! Demo Video](https://youtu.be/BHtmUCMAgPI)

## Before Getting Start
The first thing to do is to build the environment on your Raspberry Pi. Go to Terminal and enter:


```
sudo apt-get install libzbar0
pip install pyzbar
pip install RPi.GPIO
pip install opencv-python
```
To get more infomation about opencv-python, you can go to
https://docs.opencv.org/3.4.1/d2/de6/tutorial_py_setup_in_ubuntu.html

In order to create your telegram bot, you need to build the environment on your computer. Go to Terminal and enter:
```
pip install python-telegram-bot --upgrade
pip install cognitive_face
pip install pyimgur
pip install Pillow
pip install qrcode
```
## Build up your Telegram Bot
1. Download Telegram on your computer,then sign up for Telegram
https://telegram.org/apps
![](https://d1dwq032kyr03c.cloudfront.net/upload/images/20200926/20130283oUk4njEXco.png)
2. Use [@BotFather](https://t.me/BotFather) to create new bot accounts and manage your existing bots
![](https://miro.medium.com/max/698/1*oelrrJ132Ta6sp91Xo-xEQ.png)
4. Click these links to learn how to set your telegram bot
- https://ithelp.ithome.com.tw/articles/10245264
- https://hackmd.io/@truckski/HkgaMUc24?type=view#Python-Telegram-Bot-%E6%95%99%E5%AD%B8-by-%E9%99%B3%E9%81%94%E4%BB%81

4. Input your token on the script "**YOUR TOKEN HERE**".

	Notice: You need to keep your token and store it safely.
```
updater = Updater("YOUR TOKEN HERE", use_context=True)
```

5. To upload image and get the url, register your application with Imgur.
![](https://i.imgur.com/JjquTA8.png)

6. Go to [Register your application](![](https://api.imgur.com/oauth2/addclient)
) to register your client. Then you will get your Client ID and Client secret

7. Input your CLIENT_ID on the script "**YOUR CLIENT ID**", then you can use PyImgur to upload the image
```
CLIENT_ID = "YOUR CLIENT ID"
PATH = "person_img.jpg"  # A Filepath to an image on your computer"
title = "Uploaded with PyImgur"
```

```
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title=title)
print(uploaded_image.title)
print(uploaded_image.link)
```

To get more infomation, you can go to [PyImgur](https://pyimgur.readthedocs.io/en/latest/)


8. Before using Face API to cognitive the age, you need to register your application with microsoft azure.
Click 
[Azure subscription](https://azure.microsoft.com/zh-tw/free/cognitive-services/) to Create account for free

![](https://azurecomcdn.azureedge.net/cvt-501c9a38819bd9ffc1ed855f2ed8b5db5e8936aed3e3a6732ff13f313a6c0ca4/images/page/free/portal-home-alt.png)

9. Once you have your Azure subscription, [create a Face resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesFace) in the Azure portal to get your key and endpoint.

10. Input your SUBSCRIPTION KEY  and REGIONAL on the script "**SUBSCRIPTION KEY**" and "**REGIONAL**"
```
# set up congnitive_face
KEY = 'SUBSCRIPTION KEY'
CF.Key.set(KEY)

# Replace with your regional Base URL
BASE_URL = 'https://REGIONAL.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)
```

To get more infomation, you can go to [Quickstart: Use the Face client library](https://docs.microsoft.com/en-us/azure/cognitive-services/face/quickstarts/client-libraries?tabs=visual-studio&pivots=programming-language-python)


12. Run the script
```
python telegram_bot.py
```
## Build up your Iot Bartender
1. Make sure that all electronic component can work normally
![](https://i.imgur.com/zCsALGT.png)


3. Set up your circuit diagram first, and make sure that all electronic component has been installed.
![](https://i.imgur.com/rHljPYQ.jpg)


3. Using `camera.py` to scan and decode QR codes with OpenCV
![](https://i.imgur.com/yG46nxj.png)

    To get more infomation, you can go to [An OpenCV barcode and QR code scanner with ZBar](https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/)

4. Run the script
```
python iotbartender.py
```

## References
a.	iot Bartender
- Smart Bartender
https://www.hackster.io/hackershack/smart-bartender-5c430e
- Pitender
https://hackmd.io/@nI3k8IIMTUuNhfYnYiVKlQ/rklX1RllU
- 原住民調酒
http://winelist.niusnews.com/post/3k2kt84

b.	telegram bot

- telegram bot api
https://core.telegram.org/bots/api
- python-telegram-bot
    
    https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/README.md
- python QR Code generator
https://pypi.org/project/qrcode/
- upload image via PyImgur
    - https://pyimgur.readthedocs.io/en/latest/
    - https://ithelp.ithome.com.tw/articles/10241006

c.	Age Classification
- microsoft azure face api

    https://azure.microsoft.com/zh-tw/services/cognitive-services/face/#features
