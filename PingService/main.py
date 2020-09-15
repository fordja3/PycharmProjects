from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/ping', methods=['GET'])
def ping():
    return "get request"

print(os.environ['APP_SETTINGS'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

