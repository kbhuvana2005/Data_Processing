📊**Data Processing Techniques**

📘 Overview

This project was developed as part of the Data Processing Challenge. It demonstrates various techniques and frameworks for handling large-scale and real-time data efficiently.

The project is divided into four main tasks, each focusing on a different data processing approach using Apache Spark, Apache Kafka, and Python.

**Tools and Technologies:**

Apache Kafka for real-time data streaming and message handling.

Apache Flink or Spark for stream processing and in-memory computing.

Python for building the data processing logic and machine learning models.

Jupyter Notebooks or Python scripts for submissions.

🚀 Tasks Overview
🧩 Task 1: Data Preprocessing

Goal: Clean and preprocess raw datasets using Spark.
Key Steps:

Handle missing values

Remove duplicates

Fix data type inconsistencies

Normalize and transform data

Export the cleaned data for downstream processing

📁 Folder: data_preprocessing/

**How to run:**
python preprocessing/spark_preprocessing.py

Output location:
data/processed/

**Task 2: Real-Time Data Streaming** 

**Goal**:

To create a Kafka Producer–Consumer setup that streams data in real time and performs basic processing.

**Steps to run:**

**Start Zookeeper:**

bin/zookeeper-server-start.sh config/zookeeper.properties

**Start Kafka Server:**

bin/kafka-server-start.sh config/server.properties

**Create a topic:**

bin/kafka-topics.sh --create --topic sensor_data --bootstrap-server localhost:9092

**Run Producer:**

python realtime_streaming/kafka_producer.py

**Run Consumer:**

python realtime_streaming/kafka_consumer.py


**Task 3: Incremental Data Processing** 

**Goal:**

To simulate Change Data Capture (CDC) where the model updates automatically when new data arrives.

**Steps to run:**

**Start Zookeeper:**

bin/zookeeper-server-start.sh config/zookeeper.properties


**Start Kafka Server:**

bin/kafka-server-start.sh config/server.properties


**Create topic:**

bin/kafka-topics.sh --create --topic customer_updates --bootstrap-server localhost:9092

**Run Producer:**

python incremental/kafka_cdc_producer.py

**Run Consumer:**

python incremental/kafka_cdc_consumer.py

**Note:**

The .pkl model file will be created automatically when the consumer runs.
It should not be uploaded to GitHub.


**Task 4: In-Memory Data Processing**

**Goal:**

To use Apache Spark’s in-memory processing to analyze large datasets efficiently and show improved performance.

**How to run:**

python in_memory/in_memory_processing.py

**Requirements**


Install all dependencies before running:

pip install -r requirements.txt

Install and configure Spark

**requirements.txt**

pyspark

kafka-python

pandas

numpy
scikit-learn


**Notes**:

Dataset used: marketing_campaign.csv from Kaggle

Paths can be modified based on your local setup

.pkl or output data files are not included in the repository

Each task runs independently

**📁Folder Structure**:

Data_Processing/
│
├── data_preprocessing/
│   ├── scripts/
│   └── output/
│
├── realtime_streaming/
│   ├── kafka_producer.py
│   ├── spark_streaming.py
│   └── images/
│
├── incremental_processing/
│   ├── cdc_script.py
│   └── logs/
│
├── in_memory_processing/
│   ├── in_memory_analysis.py
│   └── results/
│
└── README.md
                  
