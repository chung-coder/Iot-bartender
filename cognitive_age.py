# import
import cognitive_face as CF
import requests
import json

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# set up congnitive_face
KEY = 'SUBSCRIPTION KEY'
CF.Key.set(KEY)

# Replace with your regional Base URL
BASE_URL = 'https://REGIONAL.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)


def cognitive_age(image_url):
    # set up the url of th e person picture
    person_img_url = image_url

    # person_img_url.show()
    faces = CF.face.detect(person_img_url, attributes="age")

    #print(json.dumps(faces, sort_keys=True, indent=2))

    # 辨識人臉並畫出框線

    def getRectangle(faceDictionary):
        rect = faceDictionary['faceRectangle']
        left = rect['left']
        top = rect['top']
        bottom = left + rect['height']
        right = top + rect['width']
        return ((left, top), (bottom, right))

    # download the image from the url

    response = requests.get(person_img_url)

    person_img = Image.open(BytesIO(response.content))

    # person_img.show()

    # for each face returned use the face rectangle and draw a red box.
    draw = ImageDraw.Draw(person_img)
    for face in faces:
        draw.rectangle(getRectangle(face), outline='red', width=3)
        # print('location of the face: ')
        # print(getRectangle(face))

    # set font
    age = str(int(face['faceAttributes']['age']))
    largefont = ImageFont.truetype("ARLRDBD.TTF", 50)
    draw = ImageDraw.Draw(person_img)
    imgWidth = face['faceRectangle']['width']/2 - 5
    draw.text((face['faceRectangle']['left']+imgWidth, face['faceRectangle']['top']-55), age,
              font=largefont, fill=(255, 0, 0, 255))

    # display the image in the users default image browser.
    # person_img.show()

    return age, person_img
