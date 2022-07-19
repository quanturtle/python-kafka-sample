from kafka import KafkaConsumer

consumer = KafkaConsumer('example')

for message in consumer:
    print(message)
