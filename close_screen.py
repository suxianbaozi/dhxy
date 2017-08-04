# _*_ coding:UTF-8 _*_
from PIL import Image,ImageDraw,ImageEnhance,ImageFilter
from PIL import Image, ImageGrab
from dahua import *



class Wuhuan:
    def __init__(self):
        self.end = True
        self.not_have_mission = 0

    def go_get_mission(self):
        time.sleep(3)
        mouse_click(891,573)
        time.sleep(1)
        mouse_click(426,197)
        time.sleep(1)
        mouse_click(979,488)
        time.sleep(1)
        mouse_click(1019,613)
        time.sleep(1)
        mouse_click(1335,269)
        #领任务
        time.sleep(10)
        mouse_click(1162,688)
        time.sleep(2)




    def go(self):
        self.go_get_mission()
        time.sleep(60*8)
        go_back_beiju()

if __name__ == "__main__":
    time.sleep(3)
    Wuhuan().go()
