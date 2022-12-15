from sqlalchemy import create_engine
import pandas as pd
import requests
from pyecharts.charts import *
from pyecharts import options as opts

def WorldBar():

    # 初始化数据库连接，使用pymysql模块
    engine = create_engine(
        "mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', 'welcome2019', '127.0.0.1:3306', 'datascience',
                                                        'utf8mb4'))

    # 查询语句，选出employee表中的所有数据
    sql = '''
          SELECT provinceName,curedCount,deadCount,confirmedCount,thedate FROM world
          WHERE thedate='2020-05-20 00:00:00'
          '''
    # read_sql_query的两个参数: sql语句， 数据库连接
    global_data = pd.read_sql_query(sql, engine)

    # 输出employee表的查询结果

    serious = global_data['confirmedCount'].nlargest(15, keep='all')
    serious = global_data.iloc[serious.index]

    x_data = list(serious['provinceName'])
    # 确诊
    y1_data = list(serious['confirmedCount'])
    # 治愈
    y2_data = list(serious['curedCount'])
    # 死亡s
    y3_data = list(serious['deadCount'])
    bar = (Bar()
        .add_xaxis(x_data)
        .add_yaxis('累计确诊', y1_data, color='#10aeb5')
        .add_yaxis('累计治愈', y2_data, color='#e83132')
        .add_yaxis('累计死亡', y3_data, color='#000000')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(title='爆发国家疫情条形图')
    ))

    return bar