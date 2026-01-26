from pyspark import SparkContext
import os
sc = SparkContext("local[2]", "TextFileExample")

rdd = sc.textFile(r"C:/Users/Capricon/Desktop/new_1.txt")

os.environ["PYSPARK_PYTHON"]="C:/Users/Capricon/Documents/Python/Python37/python.exe"

rdd1=rdd.flatMap(lambda x: x.split(" "))
print(rdd1.collect())
