# _*_ coding:UTF-8 _*_
from PIL import Image,ImageDraw,ImageEnhance,ImageFilter
from PIL import Image, ImageGrab
from dahua import *



class Baotu:
    def __init__(self):
        self.end = True
        self.not_have_mission = 0

    def go_get_mission(self):
        time.sleep(3)
        mouse_click(891,573)
        time.sleep(2)
        mouse_click(426,197)
        time.sleep(2)
        mouse_click(979,488)
        time.sleep(2)
        mouse_click(1151,763)
        time.sleep(2)
        mouse_click(1335,269)
        time.sleep(10)
        mouse_click(1150,601)
        time.sleep(2)



    def auto_click_mission(self):
        while True:
            if not checkZhandou():
                if checkIsMission('宝图任务'):
                    message('在任务中'.decode('utf8'))
                    self.not_have_mission = 0
                    mouse_click(1249,358)
                else:
                    self.not_have_mission += 1
                    message(('不在任务第%d次'%(self.not_have_mission)).decode('utf8'))
                    if self.not_have_mission > 5:
                        #已经结束
                        #回悲剧
                        go_back_beiju()
                        break

            time.sleep(3)

    def go(self):
        self.go_get_mission()
        self.auto_click_mission()


if __name__ == "__main__":
    Baotu().go()
