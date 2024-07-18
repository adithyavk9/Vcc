#flask application

from flask import Flask
import os 
app = Flask(__name__)

@app.route('/', methods = ['get'])

def home():
  return ("Hello Adithya")
if __name__== "_main_":
 app.run(debug=True,host="0.0.0.0", port = 5000) 
