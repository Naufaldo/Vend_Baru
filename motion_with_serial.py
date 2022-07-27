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
    dType.dSleep(1000)

    #cone
    dType.SetPTPCmdEx(api, 1,-10, -260, 60, 0, 1)  

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
                screensaver()
                # dType.SetPTPCmd(api, 1, 10, 280, 95, 0, 1)
                # dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
                # dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)
                # print('S1 ON')
                # print(x)
                a=1
        elif x == ('9'.encode('utf-8')):
            print('S1 OFF')
            # print(x)
            a=0         

        if x == ('2'.encode('utf-8')):
            if b==0 :
                #atur parameter
                dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
                dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)

                #motion circle
                dType.SetCircleCmd(api, (25,280,95,0),(10, 270, 95, 0), 3, 1)
                # print('S2 ON')
                # print(x)
                b=1
        elif x == ('8'.encode('utf-8')):
            print('S2 OFF')
            # print(x)
            b=0   

        if x == ('3'.encode('utf-8')):
            if  c==0 :
                dType.SetPTPJointParams(api, 90, 90, 90, 90, 90, 90, 90, 90, 1)
                dType.SetPTPCoordinateParams(api, 100, 100, 100, 100,  1)

                #Ke costumer
                dType.SetPTPCmd(api, 1, 210, -175, -40, 0, 1)
                # print('S3 ON')
                # print(x)
                c=1
        elif x == ('7'.encode('utf-8')):
            print('S3 OFF')
            # print(x)
            c=0   

        if x == ('4'.encode('utf-8')):
            if  d==0:
                dType.SetPTPCmd(api, 1,260, 0, 30, 0, 1)
                # print('S4 ON')
                # print(x)
                d=1
                e=0
        elif x == ('6'.encode('utf-8')):
            print('S4 OFF')
            # print(x)
            d=0 
            # else :
            #     print(x, 'nothing')
