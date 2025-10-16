**DATA PROCESSING CHALLENGE**                                                         

This project is done for the Data Processing Challenge, which includes four main tasks:

1.Data Preprocessing

2.Real-Time Data Streaming

3.Incremental Data Processing (CDC)

4.In-Memory Data Processing

**Tools and Technologies:**

Apache Kafka for real-time data streaming and message handling.

Apache Flink or Spark for stream processing and in-memory computing.

Python for building the data processing logic and machine learning models.

Jupyter Notebooks or Python scripts for submissions.

**Task 1: Data Preprocessing** 

**Goal:**

To clean and preprocess the dataset using Spark.

The steps include:

1.Handling missing values

2.Removing duplicates

3.Fixing data types

4.Normalization / standardization

5.Feature engineering (adding new columns)

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
