import DobotDllType as dType
import time
import keyboard
# ser = serial.Serial('COM3',115200)

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

# note : set home 200,0,30
def screensaver():
    #screen saver
    while (True):
        dType.SetPTPCmdEx(api, 0, 235, 185, 29, 0, 1)
        dType.SetPTPCmdEx(api, 0, 230, -185, 29, 0, 1)
        dType.SetPTPCmdEx(api, 0, 185, -155, 35, 0, 1)
        dType.SetPTPCmdEx(api, 0, 225, 105, 35, 0, 1)
        dType.dSleep(1000)
        
        if keyboard.read_key() == "a" :
            b = 1
            break
        
       
       

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

    dType.SetIOMultiplexing(api, 15, 1, 1)
    dType.SetIOMultiplexing(api, 14, 1, 1)


    while(True) : 
            # print(dType.GetIODI(api, 15))
            #print(dType.GetIOADC(api, 15))
            #print(dType.GetIODI(api, 12))
            dType.SetIODO(api, 15, 1, 1)
            dType.SetIODO(api, 14, 1, 1)

            lambat2()
            customer()
            dType.dSleep(2000)
            home()
            cepat()
            pre_cone()
            dType.SetIODO(api, 14, 1, 1)
            dType.SetIODO(api, 15, 0, 1)
            dType.dSleep(5000)
            lambat1()
            circle()
            after_cone()
            dType.dSleep(1000)
            pre_cone()
            dType.SetIODO(api, 14, 0, 1)
            dType.SetIODO(api, 15, 1, 1)
            cepat()
            home()
            dType.SetIODO(api, 15, 1, 1)
            dType.SetIODO(api, 14, 1, 1)
            lambat2()
            customer()
            dType.dSleep(3500)
            home()
            break
    


    #screensaver()  
    #customer()
    #pre_cone()
    #circle()
    #home()
    #customer()



