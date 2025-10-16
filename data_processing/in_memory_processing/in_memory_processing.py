import os
import findspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# --- Environment setup ---

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = "/home/kbhuv/spark-3.5.1-bin-hadoop3"

findspark.init()

# --- Initialize Spark Session ---

spark = SparkSession.builder \
    .appName("In-Memory Data Processing") \
    .master("local[*]") \
    .getOrCreate()

print("Spark Session started successfully!")

# --- Load dataset ---

data_path = "/mnt/e/OneDrive/Desktop/dpt/data_processing/in_memory_processing/your_dataset.csv"

# Try reading with tab delimiter first (if not tab-separated, it will fall back)
try:
    df = spark.read.csv(data_path, header=True, inferSchema=True, sep="\t")
    if len(df.columns) == 1:  # likely not tab-separated
        raise ValueError("Detected single-column load, switching to comma separator")
except Exception as e:
    df = spark.read.csv(data_path, header=True, inferSchema=True, sep=",")
    print("Switched to comma-separated CSV reading.")

print("Dataset loaded into memory!")
df.printSchema()

# --- Data Cleaning ---

# Remove any rows with missing essential values

df_clean = df.dropna()

rows_before = df.count()
rows_after = df_clean.count()
print(f"Rows before cleaning: {rows_before}, after cleaning: {rows_after}")

# --- Create 'Age' Column ---

current_year = 2025
if "Year_Birth" in df_clean.columns:
    df_clean = df_clean.withColumn("Age", lit(current_year) - col("Year_Birth"))
else:
    print("'Year_Birth' column not found — skipping Age calculation.")

# --- Filter data ---

if all(colname in df_clean.columns for colname in ["Income", "MntWines", "MntFruits"]):
    filtered_df = df_clean.select("Age", "Income", "MntWines", "MntFruits").filter(col("Income") > 40000)
    print("Filtered records where Income > 40000:")
    filtered_df.show(10)
else:
    print("Some columns missing for filtering (check dataset header).")

print("In-memory processing completed successfully!")

spark.stop()

