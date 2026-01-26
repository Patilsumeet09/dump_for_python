import os
os.environ["PYSPARK_PYTHON"] = r"C:/Users/Capricon/Documents/Python/Python37/python.exe"

from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("app1").master("local[*]").getOrCreate()
from pyspark.sql.functions import col,when

def fun1 ():
    employees=[(1, 25, 30000),(2, 45, 50000),(3, 35, 40000)]
    ddlschema=("id","age","salary")
    df=spark.createDataFrame(employees,ddlschema)
    df.createOrReplaceTempView("emp")
    df1=spark.sql("""select id,age,salary,
                     case when(age<30 and salary<35000) then 'young & low' 
                         when (age between 30 and 40) and (salary between 35000 and 45000) then 'mid & low'
                         else 'old & high' end as cat from emp """)


    df2=df.select(
        col("id"),col("age"),\
        when((col("age")<30) & (col("salary")<45000),"young & low")\
        .when((col("age").between(30,40)) & (col("salary").between(35000,45000)),"mid & low")\
        .otherwise("old & high").alias("cat"))

    print('sql',end=" ")
    df1.show()
    print('dataframe', end=' ')
    df2.show()


fun1()




