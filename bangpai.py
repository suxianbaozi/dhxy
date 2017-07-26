# _*_ coding:UTF-8 _*_
from PIL import Image,ImageDraw,ImageEnhance,ImageFilter
from PIL import Image, ImageGrab
from dahua import *



class Bangpai:
    def __init__(self):
        self.end = True
        self.not_have_mission = 0

    def go_get_mission(self):
        time.sleep(3)
        mouse_click(994,871)
        time.sleep(2)
        mouse_click(502,789)
        time.sleep(2)
        mouse_click(520,188)
        time.sleep(2)
        mouse_click(1092,454)
        time.sleep(2)
        mouse_click(1021,271)

        time.sleep(5)
        mouse_click(1144,607)
        time.sleep(1)


    def checkIsMission(self,name):
        missionImage = ImageGrab.grab((1160,318,1200,338))
        enhancer = ImageEnhance.Contrast(missionImage)
        im = enhancer.enhance(3)
        #将图片转换成灰度图片
        missionImage = missionImage.convert("L")
        twoValue(missionImage)

        #missionImage.save("text/%s.png"%name.decode('utf8'))

        imageText = Image.open("text/%s.png"%name.decode('utf8'))
        #将图片转换成灰度图片
        imageText = imageText.convert("L")

        return diffTwoImage(missionImage,imageText)

    def auto_click_mission(self):
        while True:
            if not checkZhandou():
                if self.checkIsMission('帮派'):
                    message('在任务中'.decode('utf8'))
                    self.not_have_mission = 0
                    mouse_click(1249,358)
                else:


                    #判断买武器
                    if checkIsBuyPower():
                        mouse_click(1162,757)
                        self.not_have_mission = 0
                        time.sleep(1)
                        continue

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
    time.sleep(3)
    Bangpai().go()
