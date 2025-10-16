from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("CDC Producer started... Sending simulated updates to Kafka.")

while True:
    # Simulate a CDC event (like a customer update)
    update_event = {
        "customer_id": random.randint(1000, 2000),
        "new_income": random.randint(50000, 150000),
        "new_spending_score": round(random.uniform(30, 90), 2),
        "event_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send("customer_updates", update_event)
    print("Sent CDC event:", update_event)
    time.sleep(3)
