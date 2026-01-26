import os


os.environ["PYSPARK_PYTHON"] = r"C:/Users/Capricon/Documents/Python/Python37/python.exe"
#os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:/Users/Capricon/Documents/Python/Python37/python.exe"

from pyspark import SparkContext

sc = SparkContext("local", "TestPython")

rdd = sc.textFile(r"C:/Users/Capricon/Desktop/new_1.txt")
rdd1 = rdd.flatMap(lambda x: x.split(" "))
rdd2=rdd1.map(lambda x: (x,1))
rdd3=rdd2.reduceByKey(lambda x,y:x+y)
rdd4=rdd3.filter(lambda x:x[1]==2)


print(rdd4.collect(),end=' ')
