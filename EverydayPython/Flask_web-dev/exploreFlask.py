from flask import Flask, make_response

app = Flask(__name__)


@app.route('/string/')
def return_string():
    return 'Hello, World'


@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}
    return make_response('Hello World!', status=200, headers=headers)


@app.route('/tuple/')
def return_tuple():
    return 'Hello, World!', 200, {'Content-Type':'text/plain'}


if __name__ == '__main__':
    app.run()