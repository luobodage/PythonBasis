# -*- coding: UTF-8 -*-


# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/2/5 11:14
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
from pyecharts import options as opts
from pyecharts.charts import Scatter
import pandas as pd

data = pd.read_csv('data01.csv')

from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType

# c = (
#     PictorialBar()
#         .add_xaxis(list(data['id']))
#         .add_yaxis(
#         "",
#         list(data['values']),
#         label_opts=opts.LabelOpts(is_show=False),
#         symbol_size=18,
#         symbol_repeat="fixed",
#         symbol_offset=[0, 0],
#         is_symbol_clip=True,
#         symbol=SymbolType.ROUND_RECT,
#     )
#         .reversal_axis()
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title="PictorialBar-各省份人口数量（虚假数据）"),
#         xaxis_opts=opts.AxisOpts(is_show=False),
#         yaxis_opts=opts.AxisOpts(
#             axistick_opts=opts.AxisTickOpts(is_show=False),
#             axisline_opts=opts.AxisLineOpts(
#                 linestyle_opts=opts.LineStyleOpts(opacity=0)
#             ),
#         ),
#     )
#         .render("pictorialbar_base.html")
# )

from pyecharts import options as opts
from pyecharts.charts import Line


week_name_list = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
high_temperature = [11, 11, 15, 13, 12, 13, 10]
low_temperature = [1, -2, 2, 5, 3, 2, 0]

(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
        .add_xaxis(xaxis_data=list(data['id']))
        .add_yaxis(
        series_name="最高分",
        y_axis=list(data['values']),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
        .render("douban.html")
)
