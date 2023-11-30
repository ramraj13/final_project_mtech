from flask import Flask, request, jsonify

app = Flask(__name__)

received_keys = []  # List to store received keys

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    if 'key' in data:
        # If a single RSA key is received
        rsa_key = data['key']

        # Process the RSA key
        result = f"Received: {rsa_key}"

        # Add the key to the list of received keys
        received_keys.append(rsa_key)

        return jsonify({'result': result})

    elif 'request_all_keys' in data and data['request_all_keys']:
        # If a request for all received keys is received
        return jsonify({'received_keys': received_keys})

    else:
        return jsonify({'error': 'Invalid input'}), 400


@app.route('/endpoint', methods=['POST'])
def receive_data():
    data = request.form.get('data')
    # Process the received data as needed
    print("Received data:", data)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
