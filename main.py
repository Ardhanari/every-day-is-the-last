import os
import db_query
from flask import Flask, render_template, request, json

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

@app.route("/")
def home():
    
    last_poem = db_query.find_last_poem()
    last_poem['content'] = last_poem['content'].split('\\n')

    return render_template("index.html", poem=last_poem)