from pyspark import SparkConf,SparkContext
import  os                                              # 配置python解释器,这里用3.10
os.environ['PYSPARK_PYTHON']="C:/Users/l1361/AppData/Local/Programs/Python/Python310/python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,2,3,4,5])
def func(data):# 必须有参数和返回值
    return data*10

rdd2=rdd.map(func)
# rdd2=rdd.map(lambda x:x*10)
print(rdd2.collect())