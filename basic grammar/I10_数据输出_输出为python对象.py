from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/l1361/AppData/Local/Programs/Python/Python310/python.exe"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,2,3,4,5])
num=rdd.reduce(lambda x,y:x+y)# reduce聚合算子
print(num)
rdd_list=rdd.take(3)# take取前三个元素
print(rdd_list)
rdd_count=rdd.count()# count计算元素个数
print(rdd_count)