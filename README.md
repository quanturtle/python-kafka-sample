# Kafka Sample

This is a basic `kafka` setup for streaming data  
Download `kafka`
```
wget https://dlcdn.apache.org/kafka/3.2.0/kafka_2.13-3.2.0.tgz
tar -xzvf kafka_2.13-3.2.0.tgz
```

Start `kafka` environment
```
# run zookeeper service
bin/zookeeper-server-start.sh config/zookeeper.properties

# run kafka broker service
bin/kafka-server-start.sh config/server.properties
```

Create a topic
```
python create_topic.py
```

Run a `consumer`
```
python consumer.py
```

Send messages with a `producer`
```
python producer.py
```
