#!/bin/bash

# Prompt the user for a message
message=$1

# Construct the JSON payload
json_payload="{\"message\": \"$message\"}"

# Send the message using curl
#curl -X POST -H "Content-Type: application/json" -d "$json_payload" https://ramraj13.pythonanywhere.com/receive_message

curl -X POST -H "Content-Type: application/json" -d "$json_payload" http://127.0.0.1:5001/receive_message


# Assuming Tor is running and using the default SOCKS proxy address and port
#curl --socks5 127.0.0.1:9050 -X POST -H "Content-Type: application/json" -d "$json_payload" https://ramraj13.pythonanywhere.com/receive_message
exit()