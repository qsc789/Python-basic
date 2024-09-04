from pyspark import SparkConf,SparkContext

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

# 通过parallelize()方法将Python对象加载到Spark内，成为RDD对象
rdd1=sc.parallelize([1,2,3,4,5])
rdd2=sc.parallelize((1,2,3,4,5))
rdd3=sc.parallelize("abcdefg")
rdd5=sc.parallelize({"key1":"value1","key2":"value2"})

# 查看RDD内容需要
print(rdd1.collect())