from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/l1361/AppData/Local/Programs/Python/Python310/python.exe"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,2,3,4,5])
# 过滤数据
rdd1=rdd.filter(lambda x:x%2==0)
print(rdd1.collect())