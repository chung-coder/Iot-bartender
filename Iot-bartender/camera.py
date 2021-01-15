import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import json

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

def run():
    try:
        while True:
            _, frame = cap.read()
            
            decodedObjects = pyzbar.decode(frame)
            data = 0

            for obj in decodedObjects:
                print(str(obj.data, 'utf-8'))
                cv2.putText(frame, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)
                data = json.loads(json.dumps(eval(str(obj.data, 'utf-8'))))
                break
                
            cv2.imshow("Frame", frame)

            if data != 0:
                type = data['type']
                ratio = data['ratio']
                return type,ratio
            
    except KeyboardInterrupt:
        key = cv2.waitKey(1)
        if key == 27:
            return
    
  
