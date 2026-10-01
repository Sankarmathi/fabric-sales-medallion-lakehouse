# 02_silver_cleanse.py - Silver Layer Cleansing
# Sankarmathi V - DP-600 Project

from pyspark.sql.functions import col, to_date, when

# Read from Bronze Delta
df = spark.read.format("delta").load("Files/Bronze/sales")

# Cleanse: Dedupe, Handle Nulls
df_clean = df.dropDuplicates(["SalesID"]) \
  .filter(col("Amount") > 0) \
  .filter(col("SalesID").isNotNull()) \
  .withColumn("SalesDate", to_date(col("SalesDate"), "yyyy-MM-dd"))

# Write to Silver with V-Order
df_clean.write.format("delta").mode("overwrite").option("delta.vOrder", "true").save("Tables/silver_sales")

print(f"Silver records: {df_clean.count()}")
