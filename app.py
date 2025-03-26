from flask import Flask, jsonify, render_template, request
import sqlite3

from db_operations import * 
from db_queries import *

app = Flask(__name__)

# Path to our SQLite database file
DATABASE = 'db/registrar.db'




# Student routes

# Course routes

# Section routes

# API routes



# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")