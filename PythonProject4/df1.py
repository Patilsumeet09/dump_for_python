import os

#from pyspark.conf import SparkConf

os.environ["PYSPARK_PYTHON"] = r"C:/Users/Capricon/Documents/Python/Python37/python.exe"

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

s_conf=SparkConf()
s_conf.setMaster("local")
s_conf.setAppName('app1')
s_conf.set('spark.executor.memory','4g')
s_conf.set('spark.driver.memory','4g')

spark=SparkSession.builder.config(conf=s_conf).getOrCreate()

df1=spark.read.option('path',r'C:/Users/Capricon/Desktop/SAMPLE.csv')\
    .format('csv')\
    .option('mode','PERMISSIVE')\
    .option('header',True) \
    .option('inferSchema',True)\
    .load()

from pyspark import SparkContext

sc=spark.sparkContext  #sparksession(defined as spark) has sparkcontext in it
rdd = sc.textFile(r"C:/Users/Capricon/Desktop/new_1.txt")
rdd1=rdd.flatMap(lambda x: x.split(" "))
rdd2=rdd1.map(lambda x: (x,1))

df2=rdd2.toDF(['keys','values'])
#---------------+

df2.show()
df1.show(5)

df2.createOrReplaceTempView('df2_sql')

spark.sql('select * from df2_sql where keys ="scala" ').show()