import os
os.environ["PYSPARK_PYTHON"] = r"C:/Users/Capricon/Documents/Python/Python37/python.exe"
from pyspark.sql.session import SparkSession

spark=SparkSession.builder.appName("schema_trial").master('local[1]').getOrCreate()
l=[(1,"smt"),(2,"eht")]
ddlschema=["id","name"]
#df2=l.toDF(ddlschema)
sc=spark.sparkContext
rdd=sc.parallelize(l)
#print(rdd.collect())
df1=spark.createDataFrame(l,ddlschema)
#df2=spark.createDataFrame(l,ddlschema)
#df2.show()
df1.show()


df3 = spark.read.format("csv").schema("pg_schema").path("C:/Users/Capricon/Desktop/SAMPLE.csv").load()
df3.show()