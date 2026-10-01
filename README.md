# Microsoft Fabric End-to-End Data Engineering & Analytics Solution

**Technologies:** Microsoft Fabric | OneLake | Lakehouse | Data Factory | Dataflows Gen2 | PySpark | SQL | Delta Lake | Power BI | DAX

> DP-600 Certification Project | Built in Fabric 60-day Trial | Sales Domain (500K+ rows)

## 1. Business Problem
Built end-to-end sales analytics for retail business to track KPIs, customer trends, and sales performance.

## 2. Architecture - Medallion
`Source (CSV/SQL) -> Dataflows Gen2 -> Bronze (Delta Raw) -> PySpark Notebook -> Silver (Cleaned) -> MERGE SCD2 -> Gold (Star Schema) -> Power BI DirectLake`

## 3. What I Built
- **Bronze:** Ingested source data into OneLake using Data Factory pipelines & Dataflows Gen2
- **Silver:** PySpark notebooks for data cleansing, transformation, validation, business-rule implementation. Dropped duplicates, handled nulls.
- **Gold:** Implemented Delta MERGE for incremental load + SCD Type 2 for DimCustomer. Created FactSales, DimCustomer, DimProduct, DimDate (Star Schema)
- **Performance:** OPTIMIZE + V-ORDER, query reduced from 12s to 2.1s
- **Power BI:** DirectLake semantic model, DAX measures (Total Sales, YTD), RLS implementation, dashboards with KPIs, trends, filters, drill-down

## 4. Code Samples
Check `/notebooks` folder:
- `02_silver_cleanse.py` - Dedupe & cleanse
- `03_gold_scd2_merge.py` - MERGE SCD2 logic

## 5. DAX Measures
```DAX
Total Sales = SUM(FactSales[Amount])
Sales YTD = TOTALYTD([Total Sales], DimDate[Date])
