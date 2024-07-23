#flask application

from flask import Flask, render_template_string #import flask class from flask module 
import os 
app = Flask(__name__) #This line creates an instance of the Flask class. The __name__ argument helps Flask determine the root path for the application.

@app.route('/', methods = ['GET'])

def home():
  html_content ="""<html>
  <head></head>
  <body>
  <style>
    body {
        background-color: Sienna;
        font-family: "Helvetica Neue Light", Helvetica, sans-serif;
        font-weight: 300;
        text-align: center;
      }
    </style>
    <h1>Watch out for the flying cat!</h1>
    <p>
      Here it comes:
      <img src="http://bit.ly/r3fgru" />
    </p>
  </body>
</html> """
  return render_template_string(html_content)
if __name__== "__main__":
 app.run(debug=True,host="0.0.0.0", port = 5000) 
