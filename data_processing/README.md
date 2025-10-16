🧠 Data Processing Techniques – Task Details

This document provides a detailed overview of the four tasks performed in the Data Processing Challenge using Python, Apache Spark, and Apache Kafka.

⚡ Task 1: Data Preprocessing 🧹

🎯 Goal:
Clean and prepare the dataset for analysis or modeling.

✅ Steps Done:

📥 Loaded the dataset using Spark.

🧩 Handled missing values appropriately.

🗑 Removed duplicate records to ensure data quality.

📝 Corrected column data types for consistency.

⚖ Standardized and normalized numeric features.

✨ Created new features, e.g., total customer spend or tenure.

🏁 Result:
Cleaned and processed dataset ready for downstream tasks.

⚡ Task 2: Real-Time Data Streaming 📡

🎯 Goal:
Stream data in real-time using Kafka.

✅ Steps Done:

⚙ Configured and started Zookeeper and Kafka server.

🏷 Created a Kafka topic for streaming sensor/customer data.

🚀 Implemented a Producer to continuously send data to Kafka.

📡 Implemented a Consumer to receive data and perform basic processing (filtering, transformations, logging).

🏁 Result:
Simulated real-time data flow with processing in Python.

⚡ Task 3: Incremental Data Processing (CDC) 🔄

🎯 Goal:
Automatically update data or models as new information arrives.

✅ Steps Done:

🏷 Set up Kafka topic for customer updates.

🚀 Producer sends new or updated customer records to Kafka.

📡 Consumer listens to updates and applies changes incrementally.

💾 Automatically updates the model and stores it as a .pkl file (not included in repo).

🏁 Result:
Incremental data processing demonstrated without reprocessing full datasets.

⚡ Task 4: In-Memory Data Processing ⚡

🎯 Goal:
Process large datasets efficiently using Spark’s in-memory computation.

✅ Steps Done:

📥 Loaded the processed dataset into Spark DataFrame.

🧠 Cached data in memory for improved performance.

🔄 Performed aggregations, filtering, and transformations.

⏱ Compared in-memory operations vs disk-based processing to show speed improvement.

🏁 Result:
Fast, efficient data analysis demonstrating Spark’s in-memory capabilities.
