from flask import Flask

app = Flask(__name__)  # create a python object app, which is a WSGI application
                       # WSGI(web service gateway interface)


"""Every time Flask gets a request to the '/' URL, it will call the hello function. The Python
web community calls these routed functions view functions."""


@app.route('/')
def hello():
    return 'Hello, World!'

# The final block tells Python to run a development web server, but to only do so if the current
# .py file is being called directly:
if __name__ == '__main__':
    app.run()

