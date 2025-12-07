#!/bin/bash

echo "Sending request to BTC Compression API..."

curl -X POST "https://api.btcinsights.online/compress" \
     -H "Content-Type: application/json" \
     -d '{
           "start": "2018-01-01",
           "end": "2020-01-01"
         }'
