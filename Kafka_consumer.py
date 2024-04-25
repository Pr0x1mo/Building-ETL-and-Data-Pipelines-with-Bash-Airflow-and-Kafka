
    # Create a new file named consumer.py by running the following command.

    # touch Kafka_consumer.py

from kafka import KafkaConsumer
consumer = KafkaConsumer('bankbranch',
                        group_id=None,
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset = 'earliest')
print("Hello")
print(consumer)

for msg in consumer:
    print(msg.value.decode("utf-8"))




    # Execute Kafka_admin.py and Kafka_producer.py by executing the following commands in terminal:

    # python3 Kafka_admin.py
    # python3 Kafka_producer.py

    
    # Open a new terminal and execute the following commands to run Kafka_consumer.py:

    # cd kafka_2.12-3.5.1
    # python3 Kafka_consumer.py