from kafka import KafkaProducer
import json
import time
import random

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'sensor_data'

print(" Starting data stream... (press Ctrl+C to stop)")
while True:
    # Simulated sensor data
    data = {
        "sensor_id": random.randint(1, 5),
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 80.0), 2),
        "timestamp": time.time()
    }

    # Send to Kafka topic
    producer.send(topic_name, value=data)
    print(f"Sent: {data}")

    # Wait before sending next message
    time.sleep(2)


