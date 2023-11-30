# write_message.py

# Write a message to a file
with open("message.txt", "w") as file:
    file.write("Hello from the first script!")

# Start the second Python program
import subprocess
subprocess.Popen(["python3", "read.py"])
