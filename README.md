🧠 Data Processing & Streaming Assessment








A comprehensive implementation of four major data engineering tasks — Data Preprocessing, Real-Time Streaming, Incremental Processing, and In-Memory Computation — using Apache Spark, Kafka, and Python (executed in WSL).

📁 Folder Structure
data_processing/
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

⚙️ Technologies Used
Category	Tools & Frameworks
Streaming	Apache Kafka, Zookeeper
Batch & In-Memory Processing	Apache Spark (PySpark)
Programming Language	Python 3.8+
Machine Learning	Scikit-learn, Pandas, NumPy
Environment	WSL (Ubuntu)
Development & Visualization	Jupyter Notebook
🧩 Prerequisites

Ensure you have installed:

🐍 Python 3.8+

🧰 WSL with Ubuntu

☕ Java 8+ (required by Spark)

⚙️ Apache Kafka & Zookeeper (manually installed in WSL)

💾 8 GB+ RAM

🚀 Quick Start
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Data_Processing.git
cd Data_Processing

2️⃣ Set Up the Environment
chmod +x preprocessing/setup.sh
./preprocessing/setup.sh

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start Zookeeper & Kafka
# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka Broker
bin/kafka-server-start.sh config/server.properties

🧠 Challenge Overview
<details> <summary><b>🔹 Challenge 1 — Data Preprocessing (30%)</b></summary>

Location: preprocessing/

Goal: Clean and preprocess raw data using Spark.

Includes:

Handle missing values

Remove duplicates and incorrect types

Normalize/standardize numeric columns

Create engineered features

Run:

cd preprocessing
python spark_preprocessing.py


Output: Stored in data/processed/

</details>
<details> <summary><b>🔹 Challenge 2 — Real-Time Data Streaming (35%)</b></summary>

Location: realtime_streaming/

Goal: Stream live data using Kafka producer and consumer.

Includes:

Kafka producer sending continuous data

Kafka consumer processing the data in real-time

Real-time transformation & analytics

Run:

cd realtime_streaming

# Terminal 1
python kafka_producer.py

# Terminal 2
python kafka_consumer.py

</details>
<details> <summary><b>🔹 Challenge 3 — Incremental Data Processing (25%)</b></summary>

Location: incremental/

Goal: Simulate Change Data Capture (CDC) and perform incremental updates.

Includes:

CDC producer simulating record updates

Consumer applying incremental model updates

Auto model saving (model.pkl generated)

Run:

cd incremental
python kafka_cdc_producer.py
python kafka_cdc_consumer.py


📌 Note: The model.pkl file is auto-generated and not uploaded to GitHub.

</details>
<details> <summary><b>🔹 Challenge 4 — In-Memory Data Processing (10%)</b></summary>

Location: in_memory/

Goal: Use Spark’s in-memory processing for faster computation.

Includes:

RDD & DataFrame-based caching

Performance benchmarking

Comparison with on-disk processing

Run:

cd in_memory
python in_memory_processing.py

</details>
⚙️ Configuration
Kafka
Parameter	Value
Bootstrap Servers	localhost:9092
Zookeeper	localhost:2181
Default Topics	sensor_data, customer_updates
Spark
Parameter	Value
Master	local[*]
Driver Memory	4g
📊 Dataset
File	Description
marketing_campaign.csv	Customer marketing dataset from Kaggle

📂 Stored in: data/raw/

🧪 Testing

Run all validation scripts (if available):

pytest tests/

📈 Performance Metrics

Monitored across all tasks:

⏱️ Processing latency

⚡ Throughput (messages/sec)

💾 Memory efficiency

🎯 Model performance

🧰 Troubleshooting
# Check Kafka status
ps -ef | grep kafka

# Restart Zookeeper if needed
bin/zookeeper-server-start.sh config/zookeeper.properties &

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

👩‍💻 Author

Bhuvaneswari K
📧 kbhuvana2005@github.com

🗓️ October 2025

✅ Submission Checklist

 Data Preprocessing with Spark

 Real-Time Streaming with Kafka

 Incremental Processing (CDC)

 In-Memory Processing

 Performance Evaluation

 Documentation

 Clean Folder Structure

Would you like me to add a GitHub banner image (for example, a blue Spark–Kafka–Python themed header)?
