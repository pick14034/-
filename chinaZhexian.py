from sqlalchemy import create_engine
import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
import statsmodels.api as sm
from pyecharts.charts import *
from pyecharts import options as opts
import numpy as np
from sqlalchemy import create_engine
import pandas as pd

def ChinaZhexian():

    # 初始化数据库连接，使用pymysql模块
    engine = create_engine(
        "mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', 'welcome2019', '127.0.0.1:3306', 'datascience',
                                                        'utf8mb4'))

    # 查询语句，选出employee表中的所有数据
    sql = '''
          SELECT thedate,currentConfirmedCount,suspectedCount,curedCount,deadCount,seriousCount,confirmedCount FROM data_dsc 
          '''
    # read_sql_query的两个参数: sql语句， 数据库连接
    dataset = pd.read_sql_query(sql, engine)

    # 输出employee表的查询结果
    Y = dataset['confirmedCount']
    x = [i for i in range(1, 24)]
    from scipy.optimize import curve_fit
    def logistic(t, K, P0, r):  # 定义logistic函数
        exp_value = np.exp(r * (t))
        return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

    coef, pcov = curve_fit(logistic, x, Y)  # 拟合
    print(coef)  # logistic函数参数
    y_values = [logistic(i, coef[0], coef[1], coef[2]) for i in range(1, 101)]
    import statsmodels.api as sm
    Y_dead = dataset['deadCount']
    x = [i for i in range(1, 24)]
    res_dead = np.polyfit(x, Y_dead, 3, rcond=None, full=False, w=None, cov=False)
    A, B, C, D = res_dead[0], res_dead[1], res_dead[2], res_dead[3]
    Y_dead_3 = []
    for number in x:
        Y_dead_3.append(A * number * number * number + B * number * number + C * number + D)

    x_data = list(dataset['thedate'])
    # 确诊
    y1_data = list(dataset['confirmedCount'])
    # 治愈
    # y2_data =list(dataset['curedCount'])
    # 死亡
    y3_data = list(dataset['deadCount'])
    line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('累计确诊', y1_data, color='#10aeb5')
        .add_yaxis('预测确诊', y_values, color='#e83132')
        .add_yaxis('累计死亡', y3_data, color='#000000')
        .add_yaxis('预测死亡', Y_dead_3, color='#ac35ab')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(title='中国疫情随时间变化趋势')
    ))

    return line

