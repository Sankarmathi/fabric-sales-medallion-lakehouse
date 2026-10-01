# 03_gold_scd2_merge.py - Gold Layer SCD Type 2
# Sankarmathi V - DP-600 | Implements Delta MERGE for SCD2

from delta.tables import DeltaTable

# Gold SCD2 MERGE Logic for DimCustomer
spark.sql("""
MERGE INTO gold_dim_customer AS target
USING silver_customer AS source
ON target.CustomerID = source.CustomerID AND target.is_current = true
WHEN MATCHED AND target.Email <> source.Email THEN
  UPDATE SET target.is_current = false, target.end_date = current_date()
WHEN NOT MATCHED THEN
  INSERT (CustomerID, Name, Email, is_current, start_date, end_date)
  VALUES (source.CustomerID, source.Name, source.Email, true, current_date(), NULL)
""")

# Fact Table Load - Star Schema
spark.sql("""
INSERT INTO gold_fact_sales
SELECT s.SalesID, c.CustomerKey, p.ProductKey, d.DateKey, s.Amount
FROM silver_sales s
JOIN gold_dim_customer c ON s.CustomerID = c.CustomerID
JOIN gold_dim_product p ON s.ProductID = p.ProductID
JOIN gold_dim_date d ON s.SalesDate = d.Date
""")

# Performance Optimization
spark.sql("OPTIMIZE gold_fact_sales VORDER")
print("Gold layer loaded with SCD2")
