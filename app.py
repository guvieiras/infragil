#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.router('/')

def home():
        return 'OK!'


app.run(host='0.0.0.0', port='8080', debug=True)
# comentario
