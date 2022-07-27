import serial
import time
import threading
import DobotDllType as dType
ser = serial.Serial('COM1',115200)

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
    #dType.dSleep(1000)

    #cone
    #dType.SetPTPCmdEx(api, 1,-10, -260, 60, 0, 1)  
def motion1():
    dType.SetPTPCmd(api, 1, 10, 280, 95, 0, 1)
    dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
    dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)

def circle():
    dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
    dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)
    #motion circle
    dType.SetCircleCmd(api, (15,280,95,0),(10, 270, 95, 0), 3, 1)

def motion3():
    dType.SetPTPJointParams(api, 90, 90, 90, 90, 90, 90, 90, 90, 1)
    dType.SetPTPCoordinateParams(api, 100, 100, 100, 100,  1)

    #Ke costumer
    dType.SetPTPCmd(api, 1, 210, -175, -40, 0, 1)


def cone_loader():
    dType.SetPTPCmd(api, 1, 26.8, -248.6, 60, 0, 1)
    dType.SetPTPCmd(api, 1, 26.8, -248.6, 30, 0, 1)
    dType.SetPTPCmd(api, 1, 200, 0, 30, 0, 1)

def pre_cone():
    dType.SetPTPCmd(api, 1, 40, 195, 78, 0, 1)
    dType.SetPTPCmd(api, 1, 17, 262, 93, 0, 1)

def home():
    dType.SetPTPCmd(api, 1, 200, 0, 30, 0, 1)

def cost():
    # dType.SetPTPCmd(api, 1, 131, -243, 5.9, 0, 1)
    dType.SetPTPCmd(api, 1, 131, -243, 59, 0, 1)
    dType.SetPTPCmd(api, 1, 131, -243, 5.9, 0, 1)

def customer():
    dType.SetPTPCmdEx(api, 2, 200, 10, 0, 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 2, 200, 10, (-10), 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 2, 300, 10, 0, 0, 1)
    dType.SetWAITCmdEx(api, 0.1, 1)

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

    while True:   
        x = ser.read() 
        #Cone detection
        # if a==0:
        #     screensaver()
        #     a=1
        
        if x == ('1'.encode('utf-8')):
            if a==0:
                print('Mulai')
                customer()
                dType.dSleep(1000)
                pre_cone()
                dType.dSleep(1000)
                circle()
                customer()
                dType.dSleep(2000)
                home()
                # dType.SetPTPCmd(api, 1, 10, 280, 95, 0, 1)
                # dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
                # dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)
                # print('S1 ON')
                # print(x)
                a=1
        elif x == ('9'.encode('utf-8')):
            print('SCreen Saver')
            screensaver()
            # print(x)
            a=0    
            home()  
 

       
