import kafka.admin

def main():
    admin_client = kafka.admin.KafkaAdminClient(
            bootstrap_servers='localhost:9092',
            client_id='test'
    )

    new_topics = [kafka.admin.NewTopic(name='example', num_partitions=1, replication_factor=1)]
    admin_client.create_topics(new_topics=new_topics, validate_only=False)

    return

main()
