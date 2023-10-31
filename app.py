from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve data from the database
    return render_template('index_tailwind.html')

if __name__ == '__main__':
    app.run(debug=True)