# -*- coding: UTF-8 -*-


# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/19 8:43
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
import tushare as ts


def get_data(codes):
    for code in codes:
        try:
            tf = ts.get_hist_data(code)
            tf.to_csv(f'data/{code}.csv')
        except:
            print(f'{code}.csv下载失败')
            continue


get_data(['002230', '600010', '603628', '603332', '600039', '600048', '600136', '600135', '600053', '600130', '600061',
          '600063', '600155', '600157', '600346', '600101', '600225'])
