from flask import render_template
from app import app
import json
import random
import os

@app.route('/')
@app.route('/index')
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'quotes.json')
    quote_data = json.load(open(json_url))
    random.seed()
    quote = quote_data[random.randrange(0, len(quote_data))]
    return render_template('index.html', quote=quote)