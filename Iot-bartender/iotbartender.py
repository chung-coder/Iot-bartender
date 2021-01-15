import RPi.GPIO as GPIO
import camera
from time import sleep

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
relay_pins = [17, 22, 23, 24, 25, 27]
#{Pump_1(米酒):17,Pump_2(雪碧):27,Pump_3(國農牛乳):22,
# Pump_4(美粒果):23,Pump_5(咖啡):24,Pump_6(蔓越莓汁):25}
 
# loop through pins and set mode and state to 'low'
for i in relay_pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

#GPIO.HIGH -> 1
#GPIO.LOW -> 0
    
# time to sleep between operations in the main loop

SleepTime_1 = 24
SleepTime_2 = 45
SleepTime_3 = 90
SleepTime_4 = 60
SleepTime_5 = 120
SleepTime_6 = 12

def wine_1(ratio):
    if ratio == "medium":
        GPIO.output(22, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        sleep(SleepTime_2-SleepTime_1)
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1)
        
    elif ratio == "low":
        GPIO.output(22, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        sleep(SleepTime_2-SleepTime_1+SleepTime_6)
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1-SleepTime_6)
        
    elif ratio == "high":
        GPIO.output(22, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        sleep(SleepTime_2-SleepTime_1-SleepTime_6)
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1+SleepTime_6)
    print ("wine_1 has done")
    
def wine_2(ratio):
    if ratio == "medium":
        GPIO.output(25, GPIO.LOW)
        sleep(SleepTime_3-SleepTime_1)
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1)
        print ("wine_2 has done")
    
    elif ratio == "low":
        GPIO.output(25, GPIO.LOW)
        sleep(SleepTime_3-SleepTime_1+SleepTime_6)
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1-SleepTime_6)
        print ("wine_2 has done")

    elif ratio == "high":
        GPIO.output(25, GPIO.LOW)
        sleep(SleepTime_3-SleepTime_1-SleepTime_6)
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1+SleepTime_6)
        print ("wine_2 has done")
        
def wine_3(ratio):
    if ratio == "medium":
        GPIO.output(23, GPIO.LOW)
        sleep(SleepTime_4-SleepTime_1)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1)
        
    elif ratio == "low":
        GPIO.output(23, GPIO.LOW)
        sleep(SleepTime_4-SleepTime_1)
        GPIO.output(27, GPIO.LOW)
        sleep(SleepTime_6)
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1-SleepTime_6)
    
    elif ratio == "high":
        GPIO.output(23, GPIO.LOW)
        sleep(SleepTime_4-SleepTime_1)
        GPIO.output(27, GPIO.LOW)
        sleep(+SleepTime_6)
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1+SleepTime_6)
        
    print ("wine_3 has done")
    
def drink_1():
    GPIO.output(27, GPIO.LOW)
    sleep(SleepTime_5)
    print ("drink_1 has done")
    
def drink_2():
    GPIO.output(24, GPIO.LOW)
    sleep(SleepTime_5)
    print ("drink_2 has done")
    
def drink_3():
    GPIO.output(22, GPIO.LOW)
    sleep(SleepTime_5)
    print ("drink_3 has done")
    
def drink_4():
    GPIO.output(25, GPIO.LOW)
    sleep(SleepTime_5)
    print ("drink_4 has done")
    
def drink_5():
    GPIO.output(23, GPIO.LOW)
    sleep(SleepTime_5)
    print ("drink_5 has done")
    
def printInfo(type,ratio):
    
    # 飲品種類字典
    state_type = {"wine_1": "成熟的大人 - 米咖儂",
                  "wine_2": "米蔓天使 - 米蔓",
                  "wine_3": "少女心 - 米美雪",
                  "drink_1": "來點氣泡吧 - 雪碧",
                  "drink_2": "成熟的味道 - 伯朗咖啡",
                  "drink_3": "新鮮純淨 - 牛乳",
                  "drink_4": "酸甜滋味 - 蔓越莓汁",
                  "drink_5": "清涼果汁 - 美粒果",
                  }
    # 濃度字典

    state_ratio = {"regular": "無酒精成分",
                   "low": "低濃度",
                   "medium": "黃金比例",
                   "high": "高濃度",
                   }
    
    print("飲料品項為 " + state_type[type] + " ,濃度為 " + state_ratio[ratio])

def makeDrink(type,ratio):
    if type == "wine_1":
        wine_1(ratio)
    elif type == "wine_2":
        wine_2(ratio)
    elif type == "wine_3":
        wine_3(ratio)
    elif type == "drink_1":
        drink_1()
    elif type == "drink_2":
        drink_2()
    elif type == "drink_3":
        drink_3()
    elif type == "drink_4":
        drink_4()
    elif type == "drink_5":
        drink_5()
    
def main():
    type, ratio = camera.run()
    makeDrink(type,ratio)    
    GPIO.cleanup()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
        GPIO.cleanup()