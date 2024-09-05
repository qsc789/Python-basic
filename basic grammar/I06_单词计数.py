from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/l1361/AppData/Local/Programs/Python/Python310/python.exe"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.textFile("D:/hello.txt")
word=rdd.flatMap(lambda line:line.split(" "))
data=word.map(lambda word:(word,1))
count=data.reduceByKey(lambda a,b:a+b)
print(count.collect())
