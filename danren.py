# _*_ coding:UTF-8 _*_
from baotu import Baotu
from shimen import Shimen
from wuhuan import Wuhuan
from bangpai import Bangpai

def danren():
    Baotu().go()
    Shimen().go()
    Bangpai().go()
    Wuhuan().go()


if __name__ == "__main__":
    danren()
