from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/l1361/AppData/Local/Programs/Python/Python310/python.exe"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.textFile("D:/hello.txt")
word=rdd.flatMap(lambda line:line.split(" "))
data=word.map(lambda word:(word,1))
count=data.reduceByKey(lambda a,b:a+b)
final_count=count.sortBy(lambda x:x[1],ascending=False,numPartitions=1)# 排序依据，True升序False降序，分多少区排序
print(final_count.collect())