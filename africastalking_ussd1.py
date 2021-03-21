import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'HelloWorld, Web App with Python Flask!'



if __name__ == '__main__':
    app.run(debug=True)
