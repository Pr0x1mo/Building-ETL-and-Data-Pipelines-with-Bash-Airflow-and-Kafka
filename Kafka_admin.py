    # cd kafka_2.12-3.5.1

    # Install the kafka-python package by running the following command.

    # pip3 install kafka-python

    # Create a new file named admin.py by running the following command.

    # touch Kafka_admin.py
from kafka.admin import KafkaAdminClient,NewTopic
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
topic_list = []
new_topic = NewTopic(name="bankbranch", num_partitions= 2, replication_factor=1)
topic_list.append(new_topic)
admin_client.create_topics(new_topics=topic_list)
