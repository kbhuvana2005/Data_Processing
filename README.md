**DATA PROCESSING CHALLENGE**

## 📂 Project Overview

This repository includes four tasks:

1. **Data Preprocessing** – Clean and preprocess datasets.
2. **Real-Time Data Streaming** – Stream data using Kafka producer–consumer setup.
3. **Incremental Data Processing (CDC)** – Update models automatically as new data arrives.
4. **In-Memory Data Processing** – Use Spark’s in-memory capabilities for efficient analysis.

---
## 🚀 Features

* Handle missing values, duplicates, and inconsistent data types
* Normalize and standardize datasets
* Perform feature engineering
* Stream real-time data with Kafka
* Implement incremental updates using Change Data Capture (CDC)
* Perform high-performance in-memory data analytics using Spark

---

## 📊 Dataset

* **Source:** [Marketing Campaign Dataset (Kaggle)](https://www.kaggle.com/datasets)
* **Path:** `data/raw/marketing_campaign.csv`
* The processed outputs will be saved in `data/processed/`.

---

## 🛠 Requirements

1. **Python 3.10+**
2. **Apache Spark** – Install and configure Spark on your system
3. **Apache Kafka** – Install Kafka and Zookeeper

**Install Python dependencies:**

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
pyspark
kafka-python
pandas
numpy
scikit-learn
```

---

## ⚡ Task Details

### **Task 1: Data Preprocessing**

**Goal:** Clean and preprocess the dataset using Spark

**Steps performed:**

* Handle missing values
* Remove duplicates
* Fix data types
* Normalize / standardize
* Feature engineering

**Run:**

```bash
python preprocessing/spark_preprocessing.py
```



---

### **Task 2: Real-Time Data Streaming**

**Goal:** Stream data in real-time using Kafka

**Run steps:**

```bash
# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka Server
bin/kafka-server-start.sh config/server.properties

# Create topic
bin/kafka-topics.sh --create --topic sensor_data --bootstrap-server localhost:9092

# Run Producer
python realtime_streaming/kafka_producer.py

# Run Consumer
python realtime_streaming/kafka_consumer.py
```

---

### **Task 3: Incremental Data Processing (CDC)**

**Goal:** Simulate Change Data Capture; automatically update the model with new data

**Run steps:**

```bash
# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka Server
bin/kafka-server-start.sh config/server.properties

# Create topic
bin/kafka-topics.sh --create --topic customer_updates --bootstrap-server localhost:9092

# Run Producer
python incremental/kafka_cdc_producer.py

# Run Consumer
python incremental/kafka_cdc_consumer.py
```


---

### **Task 4: In-Memory Data Processing**

**Goal:** Use Spark’s in-memory processing to analyze large datasets efficiently

**Run:**

```bash
python in_memory/in_memory_processing.py
```

---

## 🗂 Folder Structure

```
data_processing/
│
├── data/
│   ├── raw/
│   │   └── marketing_campaign.csv
│   └── processed/
│
├── preprocessing/
│   ├── setup.sh
│   └── spark_preprocessing.py
│
├── realtime_streaming/
│   ├── kafka_producer.py
│   └── kafka_consumer.py
│
├── incremental/
│   ├── kafka_cdc_producer.py
│   └── kafka_cdc_consumer.py
│
├── in_memory/
│   └── in_memory_processing.py
│
├── requirements.txt
└── README.md
```

---

## ⚠️ Notes

* Paths can be modified based on your local setup
* Each task runs independently


---

