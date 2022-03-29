#!/usr/bin/python3

from flask import Flask, render_template

import sensors

app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    print(sensors.read_last())
    print(type(sensors.read_last()))
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
