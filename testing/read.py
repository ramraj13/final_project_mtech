# read_message.py

# Read the message from the file
with open("message.txt", "r") as file:
    message = file.read()

# Print the message
print("Message from the first script:", message)
