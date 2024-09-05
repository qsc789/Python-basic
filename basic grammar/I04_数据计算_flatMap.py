from pyspark import SparkConf,SparkContext
import  os                                              # 配置python解释器,这里用3.10
os.environ['PYSPARK_PYTHON']="C:/Users/l1361/AppData/Local/Programs/Python/Python310/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize(["aaa aaa","bbb bbb","ccc ccc"])
rdd2=rdd.flatMap(lambda x:x.split())# ['aaa', 'aaa', 'bbb', 'bbb', 'ccc', 'ccc']可以解除嵌套
print(rdd2.collect())
sc.stop()
