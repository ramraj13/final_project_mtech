# Sample list of dictionaries with IP and PID information

def tab(data):

# Sort the list of dictionaries by 'PID' in ascending order
    sorted_data = sorted(data, key=lambda x: x['PID'])

# Create a separate dictionary from the sorted data
    sorted_dict = {}
    for entry in sorted_data:
        pid = entry['PID']
        ip = entry['IP']
        sorted_dict[pid] = ip

# Print the sorted dictionary
    print(sorted_dict)
