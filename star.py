# _*_ coding:UTF-8 _*_
from PIL import Image,ImageDraw,ImageEnhance,ImageFilter
from PIL import Image, ImageGrab
from dahua import *



class Star:
    def __init__(self):
        pass
    def go_get_mission(self):
        time.sleep(3)
        mouse_click(891,573)
        time.sleep(2)
        mouse_click(426,197)
        time.sleep(2)
        mouse_click(1285,697)
        time.sleep(2)
        mouse_click(1104,422)
        time.sleep(2)
        mouse_click(1273,269)

        time.sleep(10)
        mouse_click(1150,601)
        time.sleep(1)
    def get_npc(self):
        imageScreen = ImageGrab.grab((375,152,1400,919))
        imageScreen.show()
        draw = ImageDraw.Draw(imageScreen)
        size = imageScreen.size

        text_size = (57,20)

        for x in range(0,size[0]):
            for y in range(0,size[1]):
                color = imageScreen.getpixel((x,y))
                if color[0]>190 and color[1]>190 and color[2]<70:
                    draw.point((x,y),(0,0,0))
                    point_count = 0
                    for i in range(x,x + text_size[0]):
                        for j in range(y,y + text_size[1]):
                            if i>=size[0] or j>=size[1]:
                                continue
                            color = imageScreen.getpixel((i,j))
                            if color[0]>190 and color[1]>190 and color[2]<70:

                                point_count +=1
                            else:
                                pass
                    if point_count>150:
                        print x+375,y+152,point_count
                else:
                    draw.point((x,y),(255,255,255))

        #完成之后开始寻找
        imageScreen.show()
        imageScreen.save('text/star.png')

    def go(self):
        time.sleep(3)
        self.get_npc()


if __name__ == "__main__":
    Star().go()
