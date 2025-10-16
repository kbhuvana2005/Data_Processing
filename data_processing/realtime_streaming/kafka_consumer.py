from kafka import KafkaConsumer
import json
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

# Create Kafka consumer
consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("📡 Listening for data...")

# Prepare ML model (Temperature → Humidity)
model = LinearRegression()

X_train = np.array([[20], [25], [30], [35]])  # temperature
y_train = np.array([40, 50, 65, 80])          # humidity
model.fit(X_train, y_train)

# Save model for reference
pickle.dump(model, open("streaming/model.pkl", "wb"))

for msg in consumer:
    data = msg.value
    temp = np.array([[data["temperature"]]])
    pred_humidity = model.predict(temp)[0]
    print(f"Received: {data} → Predicted Humidity: {pred_humidity:.2f}")



