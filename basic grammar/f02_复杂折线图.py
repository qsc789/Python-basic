import json
# 处理数据
f_us=open("D:/美国.txt","r",encoding="utf-8")
us_data=f_us.read()
# 去掉不符合JSON格式的开头
us_data.replace("jsonp_1629344292311_69436(","")
# 去掉不符合JSON格式的结尾
us_data=us_data[:-2]
# JSON转字典
us_dict=json.loads(us_data)
# 获取trend key
trend_data=us_dict["data"][0]["trend"]
# 获取日期数据，用于x轴
