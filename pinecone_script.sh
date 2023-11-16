#!/bin/bash

# Setting up environment variables
export PINECONE_ENVIRONMENT='<YOUR PINECONE ENVIRONMENT>'
export PINECONE_API_KEY='YOUR PINECONE APIKEY'

# Getting the project ID
PINECONE_PROJECT_ID=$(curl -s "https://controller.$PINECONE_ENVIRONMENT.pinecone.io/actions/whoami" -H "Api-Key: $PINECONE_API_KEY" | jq -r '.project_name')

# Making a POST request to the Pinecone API
curl -X POST "https://quickstart-$PINECONE_PROJECT_ID.svc.$PINECONE_ENVIRONMENT.pinecone.io/describe_index_stats" \
  -H "Api-Key: $PINECONE_API_KEY"
