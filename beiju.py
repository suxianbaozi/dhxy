#
# _*_ coding:UTF-8 _*_
import time
from control import *
from pop import bubble
from screen import closeScreen,openSecreen


def message(str) :
    bubble.startBubble(u'挂机',str+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),0)

def sheyaoxiang():

    time.sleep(3)
    mouse_click(802,898)
    time.sleep(1)
    mouse_click(1249, 863)
    time.sleep(2)  
    mouse_dclick(1162, 424)
    time.sleep(2)
    mouse_click(1026, 636)
    time.sleep(2)
    mouse_click(1320, 298)
    time.sleep(2)
    mouse_click(980, 313)
    time.sleep(2)
    mouse_move(0,0)


def log(str):
    print str + time.strftime('%H:%M:%S',time.localtime(time.time()))

def checkZhandou():
    log(u'抓取屏幕')
    im0 =ImageGrab.grab((478,228,484,234))
    color = im0.getpixel((2,2))
    log(u'抓取屏幕成功')
    if '%d%d%d'%color=='239188109':
        message('正在战斗'.decode('utf8'))
        return True
    else:
        print time.localtime()
        message('离开战斗'.decode('utf8'))
        return False
def checkXiang():
    log(u'抓取屏幕')
    imxiang = ImageGrab.grab((1037,266,1086,288))
    color = imxiang.getpixel((17,12))
    log(u'抓取屏幕成功')
    if '%d%d%d'%color=='234113111':
        return True
    else:
        return False
def checkIsDahua():
    log(u'抓取屏幕')
    imcheckopen = ImageGrab.grab((413,911,417,918))
    color = imcheckopen.getpixel((1,1))
    log(u'抓取屏幕成功')
    if '%d'*3%color=='232212180':
        message(u'当前在大话中')
        return True
    else:
        print '%d'*3%color
        message(u'当前不在大话中')
        return False

from PIL import Image, ImageGrab
if __name__ == "__main__":
    time.sleep(5)
    closeScreen()
    while True:
        time.sleep(32*60)
        openSecreen()
        time.sleep(5)
        if checkIsDahua():
            if not checkZhandou():
                message('等待5s判断是否有香'.decode('utf8'))
                #wait for 5 sec
                time.sleep(5)
                #after wait for 10 sec,check is still not in war and in dahua
                if (not checkZhandou()) and checkIsDahua():
                    if not checkXiang():
                        message('没香了，开始吃香'.decode('utf8'))
                        sheyaoxiang()
                    else:
                        message('有香'.decode('utf8'))
        time.sleep(5)
        closeScreen()
        #time.sleep(35*60)


