import jieba
from pyecharts.globals import SymbolType
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
import json
import pandas as pd
import numpy as np
import jieba
import jieba.analyse
from pyecharts import options as opts
from pyecharts.charts import Geo,Map,Bar, Line, Page,Pie, Boxplot, WordCloud
from pyecharts.globals import ChartType, SymbolType,ThemeType



def ChinaCloud():
    # 初始化数据库连接，使用pymysql模块
    engine = create_engine(
        "mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', 'welcome2019', '127.0.0.1:3306', 'datascience',
                                                        'utf8mb4'))

    # 查询语句，选出employee表中的所有数据
    sql = '''
              SELECT summary FROM data_news 
              '''
    # read_sql_query的两个参数: sql语句， 数据库连接
    dataset = pd.read_sql_query(sql, engine)
    #print(type(dataset))

    needs=[]
    for i in dataset['summary']:
        #print(i)
        needs.append(i)
    #print(needs)
    set_need = str(needs).replace('#', "")
    #print(set_need)
    cut = jieba.lcut(set_need)
    #print(cut)

    jieba_need = jieba.analyse.extract_tags(set_need, topK=80, withWeight=True)
    print(jieba_need)
    jieba_result = []
    for i in jieba_need:
            jieba_result.append(i)

    c = (
        WordCloud(init_opts=opts.InitOpts())
            .add("", jieba_result, word_size_range=[10, 70], shape=SymbolType.RECT)
            .set_global_opts(title_opts=opts.TitleOpts(title="疫情热词"))
    )
    return c