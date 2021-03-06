#
# _*_ coding:UTF-8 _*_
from control import *
from pop import bubble
from PIL import Image, ImageGrab,ImageDraw,ImageEnhance
def twoValue(image,f=140):
    draw = ImageDraw.Draw(image)
    print image.size
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            L = image.getpixel((x,y))
            #print x,y,'=',L
            if L > f:
                draw.point((x,y),255)
            else:
                draw.point((x,y),0)
def message(str) :
    print str
    bubble.startBubble(u'挂机',str+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),0)

def sheyaoxiang():

    time.sleep(3)
    mouse_click(891,573)
    time.sleep(1)
    mouse_click(1249, 863)
    time.sleep(2)  
    mouse_dclick(*find_sheyao_xiang())
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

def checkIsKillSomeBody():
    log(u'抓取屏幕')
    imcheckopen = ImageGrab.grab((1343,231,1348,235))
    color = imcheckopen.getpixel((1,1))
    log(u'抓取屏幕成功')
    if '%d'*3%color=='234113111':
        message(u'当前正要教训某人')
        return True
    else:
        print '%d'*3%color
        message(u'当前正要教训某人')
        return False


def checkIsBuyPower():
    log(u'抓取屏幕')
    imcheckopen = ImageGrab.grab((1060,729,1067,736))
    color = imcheckopen.getpixel((1,1))
    log(u'抓取屏幕成功')
    if '%d'*3%color=='255255255':
        message(u'当前正在买武器')
        return True
    else:
        print '%d'*3%color
        message(u'当前不在买武器')
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

def go_back_beiju():
    time.sleep(3)
    mouse_click(891,573)
    time.sleep(3)
    mouse_click(426,197)
    time.sleep(1)
    mouse_click(893,330)
    time.sleep(1)
    mouse_click(652,687)
    time.sleep(1)
    mouse_click(1309,269)
    time.sleep(2)

def diffTwoImage(img1,img2):
    size = img1.size
    pointCount = size[0]*size[1]

    sameCount = 0
    for x in range(img1.size[0]):
        for y in range(img1.size[1]):
            L1 = img1.getpixel((x,y))
            L2 = img2.getpixel((x,y))

            if L1==L2:
                sameCount+=1

    print sameCount/float(pointCount)
    if sameCount/float(pointCount)>0.8:
        return True
    else:
        return False

def checkIsMission(name):

    #判断是否打开任务面板
    check_mission_pannel_open()

    missionImage = ImageGrab.grab((1160,318,1240,338))
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
def find_sheyao_xiang():
    missionImage = ImageGrab.grab((891,388,1279,556))
    missionImage.save('text/1.png')

    #第一排
    color = missionImage.getpixel((41,18))
    if '%d'*3%color=='373632':
        return (936,426)


    color = missionImage.getpixel((117,18))
    if '%d'*3%color=='124125120':
        return (1009,426)


    color = missionImage.getpixel((194,18))
    if '%d'*3%color=='686865':
        return (1009+77,426)


    color = missionImage.getpixel((271,18))
    if '%d'*3%color=='121110':
        return (1009+77+77,426)


    color = missionImage.getpixel((348,18))
    if '%d'*3%color=='151513':
        return (1009+77+77+77,426)



    #第二排
    color = missionImage.getpixel((41,106))
    if '%d'*3%color=='938981':
        return (936,426+88)


    color = missionImage.getpixel((118,106))
    if '%d'*3%color=='575752':
        return (1009,426+88)


    color = missionImage.getpixel((195,106))
    if '%d'*3%color=='515147':
        return (1009+77,426+88)


    color = missionImage.getpixel((272,106))
    if '%d'*3%color=='505046':
        return (1009+77+77,426+88)


    color = missionImage.getpixel((349,106))
    if '%d'*3%color=='505046':
        return (1009+77+77+77,426+88)
def check_mission_pannel_open():
    '''检查任务面板是否打开，如果关闭自动打开'''
    log(u'抓取屏幕')
    imcheckopen = ImageGrab.grab((1132,330,1164,360))
    color = imcheckopen.getpixel((18,13))
    log(u'抓取屏幕成功')
    if '%d'*3%color=='249229208':
        message(u'任务栏已经打开')
        return True
    else:
        print '%d'*3%color
        message(u'打开任务栏')
        mouse_click(1386,346)
        time.sleep(2)
        return False
if __name__ == "__main__":
    time.sleep(3)
    check_mission_pannel_open()
