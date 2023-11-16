import csv
from confluent_kafka import Consumer, KafkaError
import pinecone

# Initialize Pinecone
pinecone.init(api_key="<YOUR PINECONE API KEY>", environment="<YOUR PINECONE ENVIRONMENT>")

def create_consumer():
    conf = {
        'bootstrap.servers': 'localhost:19092',
        'group.id': 'fraud-detection-consumer-group',
        'auto.offset.reset': 'earliest',
    }
    consumer = Consumer(conf)
    return consumer

def consume_and_index_data(consumer, topic_name):
    try:
        consumer.subscribe([topic_name])

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"{msg.topic()}:{msg.partition()} reached end at offset {msg.offset()}")
                else:
                    print(f"Error: {msg.error()}")
            else:
                print(f"Received message on {msg.topic()} partition {msg.partition()} offset {msg.offset()}")
                # Assume each message is a CSV string
                vector = [float(feature) for feature in msg.value().decode('utf-8').split(',')]
                # Use the message offset as the vector id
                vector_id = str(msg.offset())
                # Index the vector in Pinecone
                pinecone_index(vector_id, vector)

    except KeyboardInterrupt:
        pass
    finally:
        # Close down consumer to commit final offsets
        consumer.close()

def pinecone_index(vector_id, vector):
    with pinecone.Index(index_name="fraud-detection") as index:
        index.upsert([
            (vector_id, vector)
        ])

if __name__ == '__main__':
    topic_name = 'fraud-detection'
    consumer = create_consumer()
    consume_and_index_data(consumer, topic_name)
