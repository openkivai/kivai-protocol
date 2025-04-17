import json
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/intent', methods=['POST'])
def handle_intent():
    data = request.get_json()
    
    command = data.get("command")
    obj = data.get("object")
    location = data.get("location")

    if command == "set temperature" and obj == "thermostat":
        temperature = data.get("temperature")
        response = {
            "status": "success",
            "message": f"Temperature set to {temperature}°C in {location}",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "device_id": f"{location.replace(' ', '-')}-thermostat-01"
        }
    else:
        response = {
            "status": "error",
            "message": "Unsupported command",
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5001)
