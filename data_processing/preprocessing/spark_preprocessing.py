from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg, lit
from pyspark.ml.feature import StringIndexer, VectorAssembler, StandardScaler
from pyspark.ml import Pipeline

# Start Spark session
spark = SparkSession.builder \
    .appName("CustomerDataPreprocessing") \
    .getOrCreate()

# Load dataset
df = spark.read.csv("your file name", header=True, inferSchema=True)
print("=== RAW DATA ===")
df.show(5)

print("Total rows:", df.count())
print("Columns:", df.columns)

# Drop unnecessary ID column
if "ID" in df.columns:
    df = df.drop("ID")

#  Handle missing values
numeric_cols = [f.name for f in df.schema.fields if f.dataType.simpleString() in ["int", "double", "float", "bigint"]]
string_cols = [f.name for f in df.schema.fields if f.dataType.simpleString() == "string"]

# Fill numeric NaNs with mean
for c in numeric_cols:
    mean_val = df.select(avg(col(c))).first()[0]
    if mean_val is not None:
        df = df.withColumn(c, when(col(c).isNull(), lit(mean_val)).otherwise(col(c)))

# Fill string NaNs with "Unknown"
for c in string_cols:
    df = df.fillna("Unknown", subset=[c])

#  Remove duplicate rows
df = df.dropDuplicates()

# Feature Engineering
# Total spending: sum of all “Mnt…” columns
mnt_cols = [c for c in df.columns if c.startswith("Mnt")]
if mnt_cols:
    df = df.withColumn("TotalSpent", sum([col(c) for c in mnt_cols]))
else:
    df = df.withColumn("TotalSpent", lit(0))

# Family size = adults (2) + kids + teens
if "Kidhome" in df.columns and "Teenhome" in df.columns:
    df = df.withColumn("FamilySize", col("Kidhome") + col("Teenhome") + lit(2))
else:
    df = df.withColumn("FamilySize", lit(2))

# Age = 2025 - Year_Birth
if "Year_Birth" in df.columns:
    df = df.withColumn("Age", lit(2025) - col("Year_Birth"))
else:
    df = df.withColumn("Age", lit(None))

#  Encode categorical columns
categorical_cols = [c for c in ["Education", "Marital_Status"] if c in df.columns]
indexers = [StringIndexer(inputCol=c, outputCol=f"{c}_index", handleInvalid="keep") for c in categorical_cols]

#  Assemble numeric features
feature_cols = [c for c in ["Income", "Recency", "TotalSpent", "FamilySize", "Age"] if c in df.columns]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features_raw", handleInvalid="skip")
scaler = StandardScaler(inputCol="features_raw", outputCol="features_scaled", withMean=True, withStd=True)

pipeline = Pipeline(stages=indexers + [assembler, scaler])
model = pipeline.fit(df)
scaled_df = model.transform(df)

print("\n=== CLEANED & FEATURED DATA ===")
scaled_df.select(categorical_cols + feature_cols + ["features_scaled"]).show(10, truncate=False)

#  Save cleaned output
output_path = "/mnt/e/OneDrive/Desktop/dpt/data_processing/output/customer_cleaned_data"
scaled_df.write.mode("overwrite").option("header", True).csv(output_path)

print(f"\nCleaned dataset saved to: {output_path}")

spark.stop()
