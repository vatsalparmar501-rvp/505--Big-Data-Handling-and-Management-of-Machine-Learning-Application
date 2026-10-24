import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("DataFrameTransformations") \
    .master("local[1]") \
    .getOrCreate()

data = [
    (1, "Vatsal", 65000, "Surat"),
    (2, "Krish", 55000, "Vadodara"),
    (3, "Pavan", 75000, "Surat"),
    (4, "Jaimin", 80000, "Ahmedabad")
]

columns = ["ID", "Name", "Salary", "City"]

df = spark.createDataFrame(data, columns)

print("Original DataFrame:")
df.show()

print("Selected Columns:")
df.select("Name", "Salary").show()

print("Filtered Data (Salary > 60000 and City = Surat):")
df.filter(
    (col("Salary") > 60000) & (col("City") == "Surat")
).show()

print("DataFrame with Bonus:")
df.withColumn(
    "Bonus", col("Salary") * 0.10
).show()

print("DataFrame with Renamed Column:")
df.withColumnRenamed(
    "Name", "EmployeeName"
).show()

spark.stop()