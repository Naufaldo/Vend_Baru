import serial
import time
import threading
import DobotDllType as dType
from playsound import playsound
ser = serial.Serial('COM1',115200)


#Program dengan Voiceover 

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

api = dType.load()
# connect dobot usb to pc
state = dType.ConnectDobot(api, "COM5", 115200)[0]

a=0
b=0
c=0
d=0
e=0

def screensaver():
    #screen saver
    dType.SetPTPCmdEx(api, 0, 235, 185, 29, 0, 1)
    dType.SetPTPCmdEx(api, 0, 230, -185, 29, 0, 1)
    dType.SetPTPCmdEx(api, 0, 185, -155, 35, 0, 1)
    dType.SetPTPCmdEx(api, 0, 225, 105, 35, 0, 1)
    dType.dSleep(1000)
    #dType.SetPTPCmdEx(api, 0, 68, -292, 0, 0, 1)
    #dType.SetPTPCmdEx(api, 0, 68, -292, 50, 0, 1)
    #dType.SetPTPCmdEx(api, 0, 100, 282, 0, 0, 1)
    #dType.SetPTPCmdEx(api, 0, 100, 282, 50, 0, 1)

    #cone
    #dType.SetPTPCmdEx(api, 1,-10, -260, 60, 0, 1)  
def motion1():
    dType.SetPTPCmd(api, 1, 10, 280, 95, 0, 1)
    dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
    dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)

def circle():
    #motion circle
    dType.SetCircleCmd(api, (56,273,135,0),(46, 265, 135, 0), 3, 1)

def lambat2():
    dType.SetPTPJointParams(api, 70, 70, 70, 70, 70, 70, 70, 70, 1)
    dType.SetPTPCoordinateParams(api, 70, 70, 70, 70,  1)

def lambat1():
    dType.SetPTPJointParams(api, 80, 80, 80, 80, 80, 80, 80, 80, 1)
    dType.SetPTPCoordinateParams(api, 80, 80, 80, 80,  1)

def cepat():
    dType.SetPTPJointParams(api, 90, 90, 90, 90, 90, 90, 90, 90, 1)
    dType.SetPTPCoordinateParams(api, 100, 100, 100, 100,  1)

def motion3():
    dType.SetPTPJointParams(api, 90, 90, 90, 90, 90, 90, 90, 90, 1)
    dType.SetPTPCoordinateParams(api, 100, 100, 100, 100,  1)

    #Ke costumer
    dType.SetPTPCmd(api, 1, 210, -175, -40, 0, 1)


def cone_loader():
    dType.SetPTPCmd(api, 1, 26.8, -248.6, 60, 0, 1)
    dType.SetEndEffectorSuctionCup(api, 1,  1, 1)
    dType.SetPTPCmd(api, 1, 26.8, -248.6, 30, 0, 1)
    dType.SetPTPCmd(api, 1, 200, 0, 30, 0, 1)

def pre_cone():
    dType.SetPTPCmd(api, 1, 55.9347, 273.4606, 135, 78.4399, 1)

def after_cone():
    dType.SetPTPCmd(api, 1, 55.9347, 273.4606, 145, 78.4399, 1)

def home():
   dType.SetPTPCmd(api, 1, 195.6 , -41.5 , 30, 0, 1)

def cost():
    # dType.SetPTPCmd(api, 1, 131, -243, 5.9, 0, 1)
    dType.SetPTPCmd(api, 1, 131, -243, 59, 0, 1)
    dType.SetPTPCmd(api, 1, 131, -243, 5.9, 0, 1)

def customer():
    dType.SetPTPCmdEx(api, 2, 195.6, -41.5, 0, 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 2, 195.6, -41.5, (-10), 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 2, 300, -41.5, 0, 0, 1)
    dType.SetWAITCmdEx(api, 0.1, 1)

def bow():
    dType.SetPTPCmdEx(api, 2, 195.6, -41.5, 0, 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 2, 195.6, -41.5, (-10), 0, 1)

def Homing():
    dType.GetHOMEParams(api)
    dType.SetHOMEParams(api,  200,  0,  30,  0,  1)
    dType.GetHOMEParams(api)
    dType.SetHOMECmd(api, 1, 1)

def motor_mati():
    dType.SetIODO(api, 15, 1, 1)
    dType.SetIODO(api, 14, 1, 1)

def motor_Maju():
    dType.SetIODO(api, 15, 0, 1)
    dType.SetIODO(api, 14, 1, 1)

def motor_Mundur():
    dType.SetIODO(api, 15, 1, 1)
    dType.SetIODO(api, 14, 0, 1)

if (state == dType.DobotConnect.DobotConnect_NoError): 
    #Clean Command Queued
    # dType.SetQueuedCmdClear(api)
  
    #Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)
    #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)

    #set
    dType.SetPTPJointParams(api, 150, 150, 150, 150, 150, 150, 150, 150, 1)
    dType.SetPTPCoordinateParams(api, 100, 100, 100, 100,1)
    cepat()

    #Setting Parameter Input Output
    dType.SetIOMultiplexing(api, 15, 1, 1)
    dType.SetIOMultiplexing(api, 14, 1, 1)

    #Homing For Start
    Homing()
    home()
    playsound('D:\Kuliah Online\Magang\Asperio\GESS\Dobot Vending Machine\Program VB\VoiceMaker\Robot Ready.mp3')
    print("Ready")


    while True: 
        cepat()
        bow()
        playsound('D:\Kuliah Online\Magang\Asperio\GESS\Dobot Vending Machine\Program VB\VoiceMaker\Introduce 2.mp3')
        home()
        playsound('D:\Kuliah Online\Magang\Asperio\GESS\Dobot Vending Machine\Program VB\VoiceMaker\Press Start.mp3')
        x = ser.read() 
        
        #Cone detection
        # if a==0:
        #     screensaver()
        #     a=1
        #Gerakan Utama
        if x == ('1'.encode('utf-8')):
            ser.write(b'3')
            motor_mati()
            print("Gerakan Utama")
            playsound('D:\Kuliah Online\Magang\Asperio\GESS\Dobot Vending Machine\Program VB\VoiceMaker\Process.mp3')
            lambat2()
            cone_loader()
            dType.dSleep(2000)
            cepat()
            pre_cone()
            motor_Maju()
            dType.dSleep(5000)
            lambat1()
            circle()
            after_cone()
            dType.dSleep(1000)
            motor_Mundur()
            pre_cone()
            cepat()
            home()
            motor_mati()
            lambat2()
            dType.SetEndEffectorSuctionCup(api, 1,  0, 1)
            customer()
            ser.write(b'1')
            playsound('D:\Kuliah Online\Magang\Asperio\GESS\Dobot Vending Machine\Program VB\VoiceMaker\Ice Cream to Customer.mp3')
            dType.dSleep(2500)
            ser.write(b'5')
            home()
            print("Gerakan Utama Selesai")
            x
    
        elif x == ('5'.encode('utf-8')):
            Homing()
            print("Homing")
            screensaver()
            home()
            playsound('D:\Kuliah Online\Magang\Asperio\GESS\Dobot Vending Machine\Program VB\VoiceMaker\Robot Ready.mp3')
            x

        elif x == ('3'.encode('utf-8')):
            playsound('D:\Kuliah Online\Magang\Asperio\GESS\Dobot Vending Machine\Program VB\VoiceMaker\Shut Down.mp3')
            break

 

       
