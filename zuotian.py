# _*_ coding:UTF-8 _*_
from PIL import Image,ImageDraw,ImageEnhance,ImageFilter
from PIL import Image, ImageGrab
from dahua import *

class Zuotian:
    def __init__(self):
        self.end = True
        self.not_have_mission = 0

    def go_get_mission(self):
        time.sleep(3)
        mouse_click(891,573)
        time.sleep(1)
        mouse_click(426,197)
        time.sleep(1)
        mouse_click(615,301)
        time.sleep(1)
        mouse_click(849,495)

        time.sleep(1)
        mouse_click(1213,272)

        time.sleep(5)
        mouse_click(1171,618)
        time.sleep(2)

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

    def checkDoubleConfirm(self):
        image = ImageGrab.grab((924,605,943,620))
        color = '%d%d%d'%image.getpixel((18,7))
        if color == '161215179':
            return True
        return False

    def checkSecretMonster(self):
        missionImage = ImageGrab.grab((1160,395,1160+82,395+27))
        enhancer = ImageEnhance.Contrast(missionImage)
        im = enhancer.enhance(3)
        #将图片转换成灰度图片
        missionImage = missionImage.convert("L")
        twoValue(missionImage)

        #missionImage.save("text/%s.png"%"神秘妖王2".decode('utf8'))

        imageText = Image.open("text/%s.png"%"神秘妖王".decode('utf8'))
        #将图片转换成灰度图片
        imageText = imageText.convert("L")

        return diffTwoImage(missionImage,imageText)

    def auto_click_mission(self):
        while True:
            time.sleep(1)
            try:
                image = ImageGrab.grab((376,153,1398,917))
                image.save('screen/%s.png'%str(int(time.time())))
            except:
                pass


            #判断是否弹出了领取双倍的窗口
            if self.checkDoubleConfirm():
                message('自动领取双倍'.decode('utf8'))
                mouse_click(1016,635)
                time.sleep(2)
            if not checkZhandou():
                if checkIsDahua():
                    if checkIsMission('天庭降妖'):
                        message('在任务中'.decode('utf8'))
                        self.not_have_mission = 0
                        if self.checkSecretMonster():
                            message('检测到神秘妖王'.decode('utf8'))
                            mouse_click(1249,412)
                        else:
                            mouse_click(1249,358)
                    else:
                        self.not_have_mission += 1
                        message(('不在任务第%d次'%(self.not_have_mission)).decode('utf8'))
                        if self.not_have_mission > 10:
                            #已经结束
                            #回悲剧
                            go_back_beiju()
                            break

            time.sleep(2)

    def go(self):
        self.go_get_mission()
        self.auto_click_mission()


if __name__ == "__main__":
    time.sleep(3)
    Zuotian().checkDoubleConfirm()
