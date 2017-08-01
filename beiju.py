#
# _*_ coding:UTF-8 _*_
from screen import closeScreen,openSecreen
from zuotian import Zuotian
from dahua import *

if __name__ == "__main__":

    is_zuotian = False
    # closeScreen()
    while True:
        openSecreen()
        time.sleep(5)
        if checkIsDahua():
            if not checkZhandou():

                #判断是否可以做天
                print '做天条件：'.decode('utf8'),time.localtime().tm_hour,is_zuotian

                if (time.localtime().tm_hour == 8) and (not is_zuotian):
                    message('去领做天任务啦'.decode('utf8'))
                    #进入昨天逻辑
                    Zuotian().go()
                    is_zuotian = True


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
        time.sleep(31*60)
        #time.sleep(35*60)


