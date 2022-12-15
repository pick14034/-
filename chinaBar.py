
import pyecharts
import requests
from pyecharts.charts import Pie
import requests
from pyecharts.charts import *
from pyecharts import options as opts

def ChinaBar():
    url = 'http://api.tianapi.com/txapi/ncov/index?key=0fd7df4315148dc405068de771dc279e&date=2020-06-27'
    data = requests.get(url).json()
    data=data['newslist'][0]['desc']
    a=['confirmedCount','curedCount','deadCount']
    b=[]
    b.append(data['confirmedCount'])
    b.append(data['curedCount'])
    b.append(data['deadCount'])

    # 饼图
    c = (
        Pie().add(
            "",
            [list(z) for z in zip(a, b)],
            radius=["30%", "75%"],
            #center=["75%", "50%"],
            rosetype="area",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="疫情饼状图"))
    )
    #c.render('aaa.html')
    return c
