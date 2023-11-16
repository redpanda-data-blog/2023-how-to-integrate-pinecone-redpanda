# Integrating Redpanda and Pinecone for Efficient Data Processing and Fraud Detection

In the data engineering domain, efficient data retrieval and processing are critical. Vector search engines, diverging from traditional text-based search engines, operate on numerical vector representations, enabling similarity search in high-dimensional spaces. These engines are instrumental in many data-intensive tasks across various fields including image/video search, natural language processing (NLP), fraud detection, recommendation systems, and vehicle sensor data processing.

Pinecone is a specialized vector database and search-as-a-service platform designed for seamless scalability and precise vector searches. When integrated with data streaming platforms like Redpanda, it bolsters data processing pipelines by introducing advanced search capabilities. This repository explores the integration of Redpanda and Pinecone, focusing on the use case of fraud detection using the "Credit Card Fraud Detection" dataset.

## Overview

The goal is to create a robust data processing pipeline that streams transaction data, indexes it into Pinecone for efficient similarity search to identify potential fraudulent transactions in real-time.

- Prerequisites
- Python 3.11 or higher
- Redpanda installed and running
- Pinecone vector database setup
- Redpanda topics created using the rpk command-line tool
- Confluent Kafka–Python Library installed (pip install confluent-kafka)
- Fraud Detection Dataset downloaded
- Create an index in Pinecone with 28 dimensions (corresponding to the dataset dimensions)

## Instructions

### Step 1: Produce Data to a Redpanda Topic
Create a Redpanda topic named "fraud-detection".

```
rpk topic create fraud-detection
```
Execute the `produce.py` script to read data from the dataset CSV file and produce it to the "fraud-detection" topic in Redpanda.

### Step 2: Consume Data from Redpanda
Execute the `consume.py` script to consume data from the "fraud-detection" topic in Redpanda.

### Step 3: Integrate Redpanda with Pinecone
Execute the `consume_pinecone.py` script to consume data from the "fraud-detection" topic in Redpanda and index it into Pinecone.

### Step 4: Verify Vector Data Indexing
Execute the `pinecone_script.sh` script to verify that the data has been correctly uploaded and indexed in Pinecone.

### Step 5: Identify Fraudulent Transactions
Execute the f`raud_detection_script.sh` script to compare individual transaction vectors and identify potentially fraudulent transactions based on their similarity to a known fraudulent vector.
