import os
from pyspark.context import SparkContext
sc= SparkContext('local[4]','trial')
rdd=sc.textFile('C:/Users/Capricon/Desktop/new_1.txt')

rdd1=rdd.flatMap(lambda x:x.split(' '))
print(rdd1.collect())