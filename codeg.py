

import win32com.client
import pyautogui
import os
import time
import win32api, win32con

wsh = win32com.client.Dispatch("WScript.Shell")
x_pad = 412
y_pad = 209
def screenGrab():
    box = (x_pad+1, y_pad+1,x_pad+771,y_pad+504)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    pass
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
        
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
def mousePos(cord):
    win32api.SetCursorPos((cord[0],  cord[1]))

def getcords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    
if __name__ == '__main__':
    main()
    
def startGame():
    mousePos((540, 351))
    leftClick()
    time.sleep(.1)
def Kordy():
    ids = driver.find_elements_by_xpath('//*[@id]')
    cord = ids[47].text
    x,y = cord.split(",")
    x = int(x)
    y = int(y)
    return x,y



def up():
    wsh.AppActivate("MFO3 :: Gra")
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')
    time.sleep(0.1)
def down():
    wsh.AppActivate("MFO3 :: Gra")
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
    time.sleep(0.1)
def right():
    wsh.AppActivate("MFO3 :: Gra")
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')
    time.sleep(0.1)
def left():
    wsh.AppActivate("MFO3 :: Gra")
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')
    time.sleep(0.1)

def idz(X,Y):
    x,y = Kordy()
    x1=0
    y1=0
    i=0
    while(X != x):
        x,y = Kordy()
        print x,y
        if (x==x1):
            break
        elif X>x:
            right()
            x1,y1=Kordy()
        elif X<x:
            left()
            x1,y1=Kordy()
    while(Y != y):
        x,y = Kordy()
        print x,y
        if (y==y1):
            break
        elif Y>y:
            down()
            x1,y1=Kordy()
        elif Y<y:
            up()
            x1,y1=Kordy()
    if(X!=x or Y!=y):
        idz(X,Y)
