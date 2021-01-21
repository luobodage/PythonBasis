# -*- coding: UTF-8 -*-
import multiprocessing as mp

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/20 14:19
# software: PyCharm
#         =    =     =
#          =   =   =
#           =  =  =
#         ===========
#         =   萝    =
#         =   卜    =
#         =   神    =
#         =   保    =
#         =   佑    =
#         =   永    =
#         =   无    =
#         =   bug  =
#          =      =
#           =    =
#              =
import time


def teacher():
    for i in range(5):
        print('我管不了梁志超，骂我和小菜似得')
        time.sleep(0.5)


def grandmother():
    for i in range(5):
        print('老师，梁志超骂我大傻逼')
        time.sleep(0.5)


teacher_press = mp.Process(target=teacher)
grandmother_press = mp.Process(target=grandmother)

if __name__ == '__main__':
    # star = time.time()
    # teacher()
    # grandmother()
    # end = time.time()
    # print(f'用了{end - star}')
    grandmother_press.daemon = True
    teacher_press.start()
    grandmother_press.start()


    print('休息！')


