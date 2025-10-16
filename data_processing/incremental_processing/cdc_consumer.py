from kafka import KafkaConsumer
import json, pandas as pd, os

consumer = KafkaConsumer(
    'customer_updates',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Load or create the dataset
if os.path.exists("customer_data.csv"):
    df = pd.read_csv("customer_data.csv")
else:
    df = pd.DataFrame(columns=["customer_id", "income", "spending_score", "event_time"])

print("📡 Listening for CDC events...")

for message in consumer:
    event = message.value
    print("📥 Received CDC Event:", event)

    # Update or insert record
    if event['customer_id'] in df['customer_id'].values:
        df.loc[df['customer_id'] == event['customer_id'], ['income', 'spending_score']] = [
            event['new_income'], event['new_spending_score']
        ]
    else:
        df.loc[len(df)] = [
            event['customer_id'], event['new_income'], event['new_spending_score'], event['event_time']
        ]

    df.to_csv("customer_data.csv", index=False)
    print(" Updated dataset saved (customer_data.csv)")
