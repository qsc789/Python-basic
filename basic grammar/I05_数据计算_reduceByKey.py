from pyspark import SparkConf,SparkContext
import  os                                              # 配置python解释器,这里用3.10
os.environ['PYSPARK_PYTHON']="C:/Users/l1361/AppData/Local/Programs/Python/Python310/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)
# reduceByKey可以根据key自动分组，对组内value进行聚合
rdd=sc.parallelize([("aaa",10),("aaa",30),("bbb",20),("bbb",30),("bbb",40)])
# 求每个key的和
rdd1=rdd.reduceByKey(lambda x,y:x+y)
print(rdd1.collect())