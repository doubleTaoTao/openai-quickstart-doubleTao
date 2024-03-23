from flask import Flask, jsonify,request

# app = Flask('test')
# @app.route('/ping', methods=['GET'])
# def ping():
#     return 'PONG'

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=8000)

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello world!"

@app.route('/parse', methods=['POST'])
def parse():
    request = request.get_json()

    result = {
        'chun': float(1),
        'chum': bool(False),

    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)