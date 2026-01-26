import os
from pyspark import SparkContext
from pyspark.sql import SparkSession

os.environ[ "PYSPARK_PYTHON"] = "C:/Users/Capricon/Documents/Python/Python37/python.exe"

#C:\Users\Capricon\Documents\Python\Python37

# sc=SparkContext("local[4]","spark-program")
# rdd1=sc.textFile("C:/Users/Capricon/Desktop/new_1.txt")
# rdd2=rdd1.flatMap(lambda x:x.split(" "))
# rdd3=rdd2.map(lambda x:(x,1))
# rdd4=rdd3.reduceByKey(lambda x,y:x+y)
# rdd5=rdd4.sortBy(lambda x:x[1],False)
# rdd6=rdd5.take(1)
# #rdd7=rdd6.collect()
# for i in rdd6:
#     print(i)

sc=SparkContext("local[2]","new t7")
rdd1=sc.textFile("C:/Users/Capricon/Desktop/new_2.txt")
rdd2=rdd1.flatMap(lambda x:x.split(" "))
rdd3=rdd2.map(lambda x:(x,1))
rdd4=rdd3.reduceByKey(lambda a,b:a+b)
rdd5=rdd4.filter(lambda x:x[0]=="Python" or x[1]==2)
for i in rdd5.collect():
    print()


























