from pyecharts.charts import Page
from worldZhexian import WorldZhexian
from worldBar import WorldBar
from worldMap import WorldMap

def Chart_2():
    page = Page(layout=Page.DraggablePageLayout)
    # page.add(WorldMap(), WorldZhexian(),WorldBar())
    #
    # page.render("test_2.html")
    Page.save_resize_html("test_2.html",
                        cfg_file="chart_config_2.json",
                         dest="my_test_2.html")

    return page
if __name__ == '__main__':
    Chart_2()