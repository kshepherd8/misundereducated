import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def misundereducated():
    ##return render_template('templates/index.html')
    ##return render_template('index.html')
    return "Hello"
