import os

from flask import Flask, render_template, request, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy
import requests

import json

from bs4 import BeautifulSoup as BS

app = Flask(__name__)

#DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_app.db')

#app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
#db = SQLAlchemy(app)





@app.route('/', methods=['GET'])
def index():
  return "hai"

@app.route('/extract', methods=['GET'])

def index():
  w = request.args.get('url')
  r = requests.get(w)

  page = requests.get(w)

  v = page.text

  soup = BS(page.text)

  video = soup.find("video")

  SRC = soup.find("video").get("src")
  return SRC
  
@app.route('/user', methods=['POST'])
def user():
  u = User(request.form['name'], request.form['email'])
  db.session.add(u)
  db.session.commit()
  return redirect(url_for('index'))

if __name__ == '__main__':
  db.create_all()
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
