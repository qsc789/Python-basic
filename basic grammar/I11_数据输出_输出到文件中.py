from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/l1361/AppData/Local/Programs/Python/Python310/python.exe"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd1=sc.parallelize([1,2,3,4,5])
rdd2=sc.parallelize([("hello",3),("Spark",5),("Hi",7)])
rdd3=sc.parallelize([[1,3,5],[6,7,8],[11,13,15]])

rdd1.saveAsTextFile("D:/output1.txt")
rdd2.saveAsTextFile("D:/output2.txt")
rdd3.saveAsTextFile("D:/output3.txt")
