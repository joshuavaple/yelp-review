from flask import Flask, request, jsonify
import os
from executor.inferrer import Inferrer
import traceback

app = Flask(__name__)
# dynamic URL:
APP_ROOT = os.getenv('APP_ROOT', '/infer')

HOST= '0.0.0.0'
PORT_NUBER = 8080

yelp_inferrer = Inferrer()


# specifying a specific functionality in the endpoint
@app.route(APP_ROOT, methods=["POST"])
def infer():
    data = request.json
    document = data['document']
    return yelp_inferrer.infer(document)

# returns any error traceback to the console
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(stackTrace=traceback.format_exc())


if __name__ == '__main__':
    app.run(host=HOST, port=PORT_NUBER)