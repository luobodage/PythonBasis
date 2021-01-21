# -*- coding: UTF-8 -*-


# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/20 10:41
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

# import tushare as ts
#
# data = ts.get_hist_data('002230')
# data.to_csv('data1.csv')
# data.to_json('data1.json')
import pyecharts.options as opts
from pyecharts.charts import Line

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=line-marker

目前无法实现的功能:

1、最低气温的最高值暂时无法和 Echarts 的示例完全复刻
"""
import pandas as pd

data = pd.read_csv('data1.csv')

week_name_list = list(data['date'])[::-1]
opening = list(data['open'])[::-1]
closing = list(data['close'])[::-1]
(
    Line(init_opts=opts.InitOpts())
        .add_xaxis(xaxis_data=week_name_list)
        .add_yaxis(
        series_name="开盘价",
        y_axis=opening,
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
        .set_global_opts(
        title_opts=opts.TitleOpts(title="科大讯飞股票走势图", subtitle="走势图"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
        .add_yaxis(
        series_name="关盘",
        y_axis=closing,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(value=-2, name="最低", x=1, y=-1.5)]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),
    )
    #     .set_global_opts(
    #     title_opts=opts.TitleOpts(title="科大讯飞股票走势图", subtitle="走势图"),
    #     tooltip_opts=opts.TooltipOpts(trigger="axis"),
    #     toolbox_opts=opts.ToolboxOpts(is_show=True),
    #     xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    # )
        .render("stockMovement.html")
)
