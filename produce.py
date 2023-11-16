import csv
from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def produce_data(file_path, topic_name):
    # Create a Producer instance
    #conf = {'bootstrap.servers': '0.0.0.0:9092'}  # Replace with your Redpanda server address
    conf = {
    'bootstrap.servers': 'localhost:19092',
    'queue.buffering.max.messages': 1000000,
    'queue.buffering.max.kbytes': 500000
}
    producer = Producer(conf)

    # Open the CSV file
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)  # Skip header row
        for row in csv_reader:
            # Convert row to string and send to Redpanda
            # Exclude the first and last feature from each transaction
            message = ','.join(row[1:-1])
            producer.produce(topic_name, value=message, callback=delivery_report)
    # Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered
    producer.flush()

if __name__ == '__main__':
    file_path = 'creditcard_reduced.csv'  # Replace with the path to your CSV file
    topic_name = 'fraud-detection'
    produce_data(file_path, topic_name)
