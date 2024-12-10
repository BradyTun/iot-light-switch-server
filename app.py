from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the light's state (default is off)
light_state = {"status": "off"}

@app.route('/light', methods=['GET'])
def get_light_status():
    """Endpoint to get the current light state."""
    return jsonify(light_state)

@app.route('/light', methods=['POST'])
def control_light():
    """Endpoint to turn the light on or off."""
    global light_state
    data = request.json
    if not data or 'status' not in data:
        return jsonify({"error": "Invalid request"}), 400

    status = data['status']
    if status in ['on', 'off']:
        light_state['status'] = status
        return jsonify({"message": f"Light turned {status}"})
    else:
        return jsonify({"error": "Invalid status. Use 'on' or 'off'"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
