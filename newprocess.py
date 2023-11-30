import json
import findip

def read_and_sort_json(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read each line and load JSON data
            lines = file.readlines()
            json_data_list = [json.loads(line) for line in lines]

            # Sort the list of dictionaries based on the 'PID' key
            sorted_json_data = sorted(json_data_list, key=lambda x: int(x['PID']))

            return sorted_json_data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file {file_path}: {e}")
        return None

# Example usage:
file_path = 'data.json'  # Replace with the path to your JSON file
sorted_json_data = read_and_sort_json(file_path)


findip.find_next_ip(sorted_json_data)


'''if sorted_json_data:
    print("Successful!!!")
if sorted_json_data is not None:
    print("Sorted JSON data based on PID:")
    for entry in sorted_json_data:
        print(entry)'''
