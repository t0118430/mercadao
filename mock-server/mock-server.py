from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'email' in data and 'password' in data:
        if data['email'] == 'username' and data['password'] == 'password':
            return jsonify({'id': 'mock_token'}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    return jsonify({'error': 'Missing email or password'}), 400

@app.route('/orders', methods=['GET'])
def get_orders():
    mock_response_template = '''
    {
        "count": 2,
        "orders": [
            {
                "id": 2973792,
                "identifier": 940489352969266,
                "pickingLocationId": "5f0872fe13f8790049047a2c",
                "pickingLocationName": "Pingo Doce Valongo",
                "selectedTimeSlot": {
                    "date": "2024-07-19T00:00:00.000Z",
                    "startTimeInMinutes": 1080,
                    "endTimeInMinutes": 1110
                },
                "deliverySlotDate": "2024-07-19T00:00:00.000Z",
                "timezone": "Europe/Lisbon",
                "totalItems": 43
            },
            {
                "id": 2975559,
                "identifier": 402445752971031,
                "pickingLocationId": "5f0f80ec908f28003ddc61a6",
                "pickingLocationName": "Pingo Doce Lordelo",
                "selectedTimeSlot": {
                    "date": "2024-07-19T00:00:00.000Z",
                    "startTimeInMinutes": 1230,
                    "endTimeInMinutes": 1260
                },
                "deliverySlotDate": "2024-07-19T00:00:00.000Z",
                "timezone": "Europe/Lisbon",
                "totalItems": 46
            }
        ]
    }
    '''

    # Replace parts of the string dynamically
    new_date = "2024-07-20T00:00:00.000Z"
    new_location = "Pingo Doce Porto"

    mock_response = mock_response_template.replace("2024-07-19T00:00:00.000Z", new_date)
    mock_response = mock_response.replace("Pingo Doce Valongo", new_location)

    return jsonify(json.loads(mock_response)), 200

if __name__ == '__main__':
    app.run(debug=True)
