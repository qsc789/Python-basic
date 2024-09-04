"""
1.设计一个类，完成数据封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3.读取文件，产生数据对象
4.进行数据需求的逻辑计算（计算每一天销售额）
5.通过pyechars画图
"""
from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *

text_file_reader=TextFileReader("D:/2011年1月销售数据.txt")# 对象
json_file_reader=JsonFileReader("D:/2011年2月销售数据JSON.txt")# 对象

jan_data:list[Record]=text_file_reader.read_data()
feb_data:list[Record]=json_file_reader.read_data()

# 将2个月的数据合并为1个list
all_data:list[Record]=jan_data+feb_data# 相加合并
# 数据计算
data_dict={}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date]+=record.money
    else:
        data_dict[record.date] = record.money

bar=Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额柱状图.html")

