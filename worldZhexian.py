from sqlalchemy import create_engine
import pandas as pd
import statsmodels.api as sm
from pyecharts.charts import *
from pyecharts import options as opts
from scipy.optimize import curve_fit
import numpy as np


def WorldZhexian():
    # 初始化数据库连接，使用pymysql模块
    engine = create_engine(
        "mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', 'welcome2019', '127.0.0.1:3306', 'datascience',
                                                        'utf8mb4'))

    # 查询语句，选出employee表中的所有数据
    sql = '''
          SELECT distinct currentConfirmedCount,
    confirmedCount,
    curedCount,
    deadCount,
    currentConfirmedIncr,
    confirmedIncr,
    curedIncr,
    deadIncr,
    thedate 
    FROM data
          '''
    # read_sql_query的两个参数: sql语句， 数据库连接
    globalset = pd.read_sql_query(sql, engine)


    Y = globalset['confirmedCount']
    x = [i + 60 for i in range(1, 62)]

    def logistic(t, K, P0, r):  # 定义logistic函数
        exp_value = np.exp(r * (t))
        return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

    coef, pcov = curve_fit(logistic, x, Y)  # 拟合
    print(coef)  # logistic函数参数
    y_values = [logistic(i, coef[0], coef[1], coef[2]) for i in range(61, 161)]
    time = []
    for t in range(1, 31):
        time.append("2020-04-{}".format(t))
    for t in range(1, 32):
        time.append("2020-05-{}".format(t))
    for t in range(1, 31):
        time.append("2020-06-{}".format(t))
    # for t in range(1, 32):
    #     time.append("2020-07-{}".format(t))
    # for t in range(1, 32):
    #     time.append("2020-08-{}".format(t))
    # for t in range(1,31):
    #     time.append("2020-09-{}".format(t))
    # for t in range(1,32):
    #     time.append("2020-10-{}".format(t))
    # for t in range(1,31):
    #     time.append("2020-11-{}".format(t))
    # for t in range(1,32):
    #     time.append("2020-12-{}".format(t))

    x_data = list(globalset['thedate'])
    # 累计确诊
    y1_data = list(globalset['confirmedCount'])
    # 累计治愈
    y2_data = list(globalset['curedCount'])
    # 累计死亡
    y3_data = list(globalset['deadCount'])

    line = (Line()
        .add_xaxis(time)
        .add_yaxis('累计确诊', y1_data, color='#10aeb5')
        .add_yaxis('预测确诊', y_values, color='#ac12cb')
        .add_yaxis('累计治愈', y2_data, color='#e83132')
        .add_yaxis('累计死亡', y3_data, color='#000000')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(title='世界疫情随时间变化趋势')
    ))

    return line