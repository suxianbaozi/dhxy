# _*_ coding:UTF-8 _*_
import sys,os
from PIL import Image,ImageDraw,ImageEnhance,ImageFilter
import io
from control import *
from pop import bubble
from screen import closeScreen,openSecreen
from PIL import Image, ImageGrab

def message(str) :
    bubble.startBubble(u'挂机',str+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),0)


def twoValue(image):
    draw = ImageDraw.Draw(image)
    print image.size
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            L = image.getpixel((x,y))
            #print x,y,'=',L
            if L > 180:
                draw.point((x,y),255)
            else:
                draw.point((x,y),0)

#
#
# image = Image.open('C:\\Users\\admin\\Desktop\\beiju\\7.png')
# enhancer = ImageEnhance.Contrast(image)
# im = enhancer.enhance(3)
# #将图片转换成灰度图片
# image = image.convert("L")
#
# image.show()
# twoValue(image)
# image.show()
#
# image.save('2.jpg')

import time
def log(str):
    print str + time.strftime('%H:%M:%S',time.localtime(time.time()))

class Zuotian:
    def __init__(self):
        self.end = True
        self.not_have_mission = 0

    def go_get_mission(self):
        mouse_click(426,197)
        time.sleep(1)
        mouse_click(615,301)
        time.sleep(1)
        mouse_click(849,495)

        time.sleep(2)
        mouse_click(1213,272)

        time.sleep(5)
        mouse_click(1171,618)
    def checkZhandou(self):
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
    def checkIsTian(self):
        image = ImageGrab.grab((1161,349,1359,371))
        if '%d%d%d'%image.getpixel((3,4))=='255255255' and '%d%d%d'%image.getpixel((2,4))!='255255255' and '%d%d%d'%image.getpixel((3,13))=='255255255':
            return True
        return False



    def go_back_beiju(self):
        mouse_click(426,197)
        time.sleep(1)
        mouse_click(893,330)
        time.sleep(1)
        mouse_click(652,687)
        time.sleep(1)
        mouse_click(1309,269)
        time.sleep(2)



    def auto_click_mission(self):
        while True:

            if not self.checkZhandou():
                if self.checkIsTian():
                    message('在任务中'.decode('utf8'))
                    self.not_have_mission = 0
                    mouse_click(1249,358)
                else:
                    self.not_have_mission += 1
                    message(('不在任务第%d次'%(self.not_have_mission)).decode('utf8'))
                    if self.not_have_mission > 10:
                        #已经结束
                        #回悲剧
                        self.go_back_beiju()
                        break

            time.sleep(3)

    def go(self):
        self.go_get_mission()
        self.auto_click_mission()

