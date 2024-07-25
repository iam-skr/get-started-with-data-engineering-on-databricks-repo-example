# Databricks notebook source
#This notebook creates a dataframe with some sample data that can be used for a quick visualization.

data = [[1, "Elia"], [2, "Teo"], [3, "Fang"]]

# COMMAND ----------

sdf = spark.createDataFrame(data, schema="id LONG, name STRING")

# COMMAND ----------

display(sdf)

# COMMAND ----------

