from pyecharts.charts import Page
from usaZhexian import UsaZhexian
from ydlZhexian import YdlZhexian
from ydZhexian import YdZhexian

def Chart_3():
    page = Page(layout=Page.DraggablePageLayout)
    # page.add(UsaZhexian(), YdZhexian(),YdlZhexian())
    #
    # page.render("test_3.html")
    Page.save_resize_html("test_3.html",
                        cfg_file="chart_config_3.json",
                         dest="my_test_3.html")

    return page
if __name__ == '__main__':
    Chart_3()