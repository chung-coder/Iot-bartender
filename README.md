# IoT-bartender
![](https://i.imgur.com/jgNbMPh.png)

## Overview
This is an **AI bartender with Secondary verification**. Because of the working holiday in Orchid Island during the summer vacation, I want to share Original Cocktail that I met in this summer through this project.
To implement this project, I would use five drinks and rice wine. As for user, there are three steps to operate.

a.	First, user need to offer their selfie to identify age. If their age is less than 18 years old, they cannot choose rice wine as a component of drinks.

b.	Second, user need to choose the drinks what they like and the proportion what they want on their mobile device. 

c.	Third, the mobile device will generate an qr-code and user can use it to pick their drink. When they pick up their drink, AI bartender will take a photo to verify identity.

![](https://i.imgur.com/3xwcXHw.png)


## Components
### Hardward
- Raspberry Pi 3 Model B *1
- Intel® Neural Compute Stick 2 *1
- Arducam Noir Camera for Raspberry Pi *1
- DHT22 Temperature Humidity Sensor Module *1
- 4xAA battery holder *2
- AA battery
- Jumper wires
- breadboard
- 12V DC Dosing Pump Peristaltic *6
- Food Grade Silicone Tubing *3
- 8 Channel DC 5V Relay Module *1
- Bar code & QR code Scan Module *1

### Software
- Python 3.7
- Open-Vino
- Telegram


### Accessories

- 紅標米酒
- 雪碧
- 國農牛乳
- 伯朗咖啡
- 蔓越莓汁
- 美粒果
 
## My survey on the project

![](https://i.imgur.com/dfl6llD.png)

1. [Iot-bartender外型](https://www.hackster.io/hackershack/smart-bartender-5c430e)
   ![](https://imgur.com/5kCiRb9)

2. Raspberry pi 如何與Telegram Bot串接
![](https://i.imgur.com/yG46nxj.png)
- Telegram Bot 產生QR-code

    a.	使用Python packages - [qrcode 6.1](https://pypi.org/project/qrcode/)
    Install: pip install qrcode
    
    b.	Generate and Decode QR Codes in Python document
    
- Raspberry pi掃描QR-code

    a.	使用[Barcode Scanner Module](https://www.meiyagroup.com.tw/product/bar-code-qr-code-%E6%8E%83%E6%8F%8F%E8%BE%A8%E8%AD%98%E6%A8%A1%E7%B5%84/)掃描辨識模組
    
    b.	[相關使用手冊](https://www.waveshare.net/w/upload/9/95/Barcode_Scanner_Module_Quick_Start_cn.pdf)
    
    c.[利用 Web Cam 來讀取條碼](https://atceiling.blogspot.com/2017/03/raspberry-pi-zbar.html )
    
3.	如何實作2FA  (Two-factor authentication)
- Telegram Bot - Age Classification

    a.	使用者傳送圖片給telegram bot，telegram bot運用OpenCV年齡辨識，並回傳是否滿18歲的資訊
    
    b.	[OpenCV with Telegram Bot](https://github.com/LincolnUehara/bot-opencv-telegram)
    
    c.	[Age Classification using OpenCV](https://www.learnopencv.com/age-gender-classification-using-opencv-deep-learning-c-python/)

- Raspberry Pi - Face Verification

    a.將使用者傳送給telegram bot的圖片存在QR-code內，並運用Raspberry Pi拍照識別與OpenCV、OpenVINO以驗證使用者是否為同一人
    
    b.	[參考門禁系統](https://www.instructables.com/DIY-Smart-Home-Doorbell-for-Less-Than-40/?fbclid=IwAR0vGymv65HD6OJxYTl0NFnVB5m_F3yMyNyrp4spA1Qm_s4IXwan-3XveR0)、[人臉辨識解析](https://medium.com/coding-like-coffee/%E4%BA%BA%E8%87%89%E8%BE%A8%E8%AD%98-face-recognition-cffcec53a544)

4.	Telegram Bot UI設計
![](https://i.imgur.com/n2v5UWo.png)

## Implement
- telegram bot
    - using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
    - 基本設定
        - [參考文件](https://ithelp.ithome.com.tw/articles/10245264)
    - keyboard
        - [ReplyKeyboardMarkup](https://ithelp.ithome.com.tw/m/articles/10247929)
        - [Inline keyboard&callback_query](https://ithelp.ithome.com.tw/m/articles/10248455)
    - Python Telegram Bot 教學
        - [參考文件](https://hackmd.io/@truckski/HkgaMUc24?type=view#Python-Telegram-Bot-%E6%95%99%E5%AD%B8-by-%E9%99%B3%E9%81%94%E4%BB%81)
    - qrcode
        - 產生QRcode
            - pip install qrcode[pil]
        - [傳送照片](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#post-an-image-from-memory)
- bartender Bot
    - 讀取qrcode
        - pip install pyzbar
        - [參考文件](https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/)
## Plan B
AI bartender with customization bartending
### Overview
This plan will be similar to the original plan. The difference is that it will cancel the feature of Secondary verification.

## References
a.	Bartender-pi
- Smart Bartender
https://www.hackster.io/hackershack/smart-bartender-5c430e
- 用 Arduino DIY 自動調酒機
https://arduino.nxez.com/2018/01/16/6-shooter-arduino-drink-mixing-station.html
- cocktail-pi
https://github.com/saubury/cocktail-pi
- Raspberry Pi Off-World Bartender
https://www.raspberrypi.org/blog/raspberry-pi-off-world-bartender/
- Pitender
https://hackmd.io/@nI3k8IIMTUuNhfYnYiVKlQ/rklX1RllU
- 原住民調酒
http://winelist.niusnews.com/post/3k2kt84

b.	telegram bot
- 設定telegram bot on raspberry-pi
https://www.instructables.com/Set-up-Telegram-Bot-on-Raspberry-Pi/
- Chatbot with raspberry-pi
https://github.com/The-Assembly/Home_automation_chatbot
- telegram bot api
https://core.telegram.org/bots/api
https://medium.com/front-end-augustus-study-notes/telegram-bot-api-1-e4ea74d3b064
- python QR Code generator
https://pypi.org/project/qrcode/
https://github.com/lincolnloop/python-qrcode
- python QR Code generate and decode
https://medium.com/better-programming/how-to-generate-and-decode-qr-codes-in-python-a933bce56fd0
- telegram bot opencv
https://github.com/meinside/telegram-bot-opencv

c.	Age Classification
- Gender & Age Classification using OpenCV Deep Learning
https://www.learnopencv.com/age-gender-classification-using-opencv-deep-learning-c-python/
- OpenCV using Python
https://blog.gtwang.org/programming/python-opencv-dlib-face-detection-implementation-tutorial/
- OpenCV with Telegram Bot
https://github.com/LincolnUehara/bot-opencv-telegram
