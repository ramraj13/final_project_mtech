#!/bin/bash

# Check if the input is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <list_of_rsa_keys>"
    exit 1
fi

# Extract the list of RSA keys from the command line arguments
rsa_keys=("$@")

for key in "${rsa_keys[@]}"; do
    # Escape newlines in the RSA key
    escaped_rsa_key=$(echo "$key" | sed ':a;N;$!ba;s/\n/\\n/g')

    # Create JSON payload for the current RSA key
    json_payload="{\"key\": \"$escaped_rsa_key\"}"

    # Send the JSON payload to the Flask app using curl
    curl --socks5 127.0.0.1:9050 -X POST -H "Content-Type: application/json" -d "$json_payload" http://ramraj13.pythonanywhere.com/process_data
done

# After sending all keys, send a request for all received keys
curl --socks5 127.0.0.1:9050 -X POST -H "Content-Type: application/json" -d '{"request_all_keys": true}' http://ramraj13.pythonanywhere.com/process_data
