#
# _*_ coding:UTF-8 _*_
from control import *
from pop import bubble
from PIL import Image, ImageGrab

def message(str) :
    print str
    bubble.startBubble(u'挂机',str+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),0)

def sheyaoxiang():

    time.sleep(3)
    mouse_click(891,573)
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

