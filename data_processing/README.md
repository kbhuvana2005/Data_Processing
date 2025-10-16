⚡ Task 1: Data Preprocessing

Goal: Clean and prepare the dataset for analysis or modeling.

Steps Done:

Loaded the dataset using Spark.

Handled missing values by filling them appropriately.

Removed duplicate records to ensure data quality.

Corrected column data types for consistency.

Standardized and normalized numeric features.

Created new features to enhance analysis, like total customer spend or tenure.

Result: Cleaned and processed dataset ready for downstream tasks.

⚡ Task 2: Real-Time Data Streaming

Goal: Stream data in real-time using Kafka.

Steps Done:

Configured and started Zookeeper and Kafka server.

Created a Kafka topic for streaming sensor/customer data.

Implemented a Producer that sends data continuously to Kafka.

Implemented a Consumer that receives data from Kafka and performs basic processing (filtering, transformations, logging).

Result: Real-time data flow simulation with processing in Python.

⚡ Task 3: Incremental Data Processing (CDC)

Goal: Update data or models automatically as new information arrives.

Steps Done:

Set up Kafka topic for customer updates.

Producer sends new or updated customer records to Kafka.

Consumer listens to updates and applies changes incrementally.

Automatically updates the model and stores it as a .pkl file (not included in repo).

Result: Demonstrated incremental data processing without reprocessing full datasets.

⚡ Task 4: In-Memory Data Processing

Goal: Efficiently process large datasets using Spark’s in-memory computation.

Steps Done:

Loaded the processed dataset into Spark DataFrame.

Cached data in memory to improve performance for repeated operations.

Performed aggregations, filtering, and transformations.

Compared in-memory operations vs disk-based processing to show performance improvement.

Result: Fast, efficient data analysis demonstrating Spark’s in-memory capabilities.
