import pyecharts
from pyecharts.charts import Bar

# print(pyecharts.__version__)

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "裤子", "袜子"])
bar.add_yaxis("商家", [5, 20, 45, 32])
bar.render()