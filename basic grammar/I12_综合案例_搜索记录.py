from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/l1361/AppData/Local/Programs/Python/Python310/python.exe"
os.environ['HADOOP_HOME']="E:/hadoop/spark-3.3.1-bin-hadoop3"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism","1")
sc=SparkContext(conf=conf)

file_rdd=sc.textFile("D:/search_log.txt")
# TODO 需求1：热门搜索时间段Top3（小时精度）
# 1.1 取出全部时间转化为小时
# 1.2 转换为（小时，1）的形式
# 1.3 分组聚合value
# 1.4 降序排序
# 1.5 取前3
res1=file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x:x[0][:2]).\
    map(lambda x:(x,1)).\
    reduceByKey(lambda a,b:a+b).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(f"热门搜索时间段Top3（小时精度）：{res1}")

# TODO 需求2：热门搜索词Top3
# 2.1取出全部搜索词
# 2.2（词，1）二元元组
# 2.3 分组聚合
# 2.4 排序
# 2.5 Top3
res2=file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x:x[2]).\
    map(lambda x:(x,1)).\
    reduceByKey(lambda a,b:a+b).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(f"热门搜索词Top3：{res2}")

# TODO 需求3：统计黑马程序员在什么时候被搜索的最多
# 3.1 过滤内容
# 3.2（小时，1）
# 3.3 分组聚合
# 3.4 排序
# 3.5 取第一个
res3=file_rdd.map(lambda x:x.split("\t")).\
    filter(lambda x:x[2]=="黑马程序员").\
    map(lambda x:(x[0][:2],1)).\
    reduceByKey(lambda a,b:a+b).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(1)
print(f"黑马程序员搜索高峰：{res3}")

# TODO 需求4：转换为JSON格式输出
# 4.1 转换为JSON格式的RDD
# 4.2 输出为文件
file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x:{"time":x[0],"user_id":x[1],"key_word":x[2],"rank1":x[3],"rank2":x[4],"url":x[5]}).\
    saveAsTextFile("D:/output_JSON")# 字典形式输出就是JSON
