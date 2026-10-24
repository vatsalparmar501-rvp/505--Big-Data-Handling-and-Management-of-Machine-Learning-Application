import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg, max, sum

spark = (SparkSession.builder
 .appName("Practical7")
 .master("local[*]")
 .getOrCreate())

data = [
  ("Vatsal", "IT", 65000),
 ("Krish", "HR", 50000),
 ("Jaimin", "IT", 72000),
 ("Pavan", "HR", 55000),
 ("Sujal", "IT", 68000)
]
df = spark.createDataFrame(data, ["Name", "Department", "Salary"])

summary = df.groupBy("Department").agg(
 count("*").alias("Employee_Count"),
 avg("Salary").alias("Average_Salary"),
 max("Salary").alias("Maximum_Salary"),
 sum("Salary").alias("Total_Salary")
)

print("Department-wise summary:")
summary.orderBy("Department").show()

print("Total number of records:", df.count())
print("Show original records:")
df.show()

spark.stop()