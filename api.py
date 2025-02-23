from flask import Flask, jsonify
from main import format_postcode, postcode_verify

app = Flask(__name__)

@app.route('/format/<postcode>', methods=['GET'])
def format_postcode_api(postcode):
    formatted_postcode = format_postcode(postcode)
    return jsonify({'status': 'success', 'formatted_postcode': formatted_postcode}), 200

@app.route('/verify/<postcode>', methods=['GET'])
def postcode_verify_api(postcode):
    try:
        postcode_verify(postcode)
        return jsonify({'status': 'success', 'message': 'Postcode is valid'}), 200
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
