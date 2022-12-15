from pyecharts.charts import Page
from chinaMap import ChinaMap
from chinaZhexian import ChinaZhexian
from chinaBar import ChinaBar
from chinaCloud import ChinaCloud

def Chart_1():
    page = Page(layout=Page.DraggablePageLayout)
    # page.add(ChinaMap(), ChinaZhexian(),ChinaBar(),ChinaCloud())
    #
    # page.render("test.html")
    Page.save_resize_html("test.html",
                        cfg_file="chart_config.json",
                         dest="my_test.html")

    return page
if __name__ == '__main__':
    Chart_1()