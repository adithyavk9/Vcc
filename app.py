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
        background-image: url("https://wallpapercave.com/wp/wp12177296.jpg"); /* Replace with your image URL */
        background-size: cover;
        background-color: #e4e3d3;
        font-family: "Helvetica Neue Light", Helvetica, sans-serif;
        font-weight: 300;
        text-align: center;
      }
.styled-paragraph {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; /* Font type */
    color: #2E2D4D; /* Font color  */
    font-size: 18px; /* Font size */
    line-height: 1.5; /* Line height */
    /*width: 180; Line width */
    font-weight: 300; /* Font weight */
    /* text-align: right; Text alignment */
    background-color: #f9f9f9; /* Background color for the paragraph */
    padding: 10px; /* Padding inside the paragraph */
    border-radius: 8px; /* Rounded corners */
    border: 1px solid #ccc; /* Border around the paragraph */
}

    </style>
  
  
    <h1 style="color: white;">Class Schedule PGDE Trimester II ! <br> <br> </h1>
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-7od5{background-color:#9aa999;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-x6qq{background-color:#D67FEB;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-90e1{background-color:#36D2A6;border-color:inherit;text-align:left;vertical-align:top}
</style>

<br>
<br>
<br>
<table class="tg" style="undefined;table-layout: fixed; width: 789px; margin-left: auto;
    margin-right: auto;"><colgroup>
<col style="width: 132.333333px">
<col style="width: 131.333333px">
<col style="width: 131.333333px">
<col style="width: 131.333333px">
<col style="width: 131.333333px">
<col style="width: 131.333333px">
</colgroup>
<thead>
  <tr>
    <th class="tg-7od5">Day\Time</th>
    <th class="tg-7od5">8 to 9:30 pm</th>
    <th class="tg-7od5">9:45 to 11:15 pm </th>
    <th class="tg-7od5">11:30 to 1 pm </th>
    <th class="tg-7od5">4 to 5:30 pm</th>
    <th class="tg-7od5">6 to 7:30 pm</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-x6qq">Saturday</td>
    <td class="tg-x6qq">Machine Learning</td>
    <td class="tg-x6qq">Social Network Analysis</td>
    <td class="tg-x6qq">Virtualization and Cloud Computing</td>
    <td class="tg-x6qq">Fundamentals of Distributed Systems</td>
    <td class="tg-x6qq">Social Network Analysis</td>
  </tr>
  <tr>
    <td class="tg-90e1">Sunday</td>
    <td class="tg-90e1">Machine Learning</td>
    <td class="tg-90e1"></td>
    <td class="tg-90e1">Virtualization and Cloud Computing</td>
    <td class="tg-90e1">Fundamentals of Distributed Systems (5 to 6:30pm)</td>
    <td class="tg-90e1"></td>
  </tr>
</tbody>
</table>
<br>
<br>
<br>
<br>
<p class="styled-paragraph">
<span style="text-align: center; display: block;font-weight: bold;"> ASSIGNMENT 1 <br>
      VIRTUALIZATION AND CLOUD COMPUTING <br></span>
    <span style="text-align: right; display: block;">  Submitted by <br>
      ADITHYA V K <br>
      Roll No : G23AI2042 <br>
      </span>
    </p>
</body>
</html> """
  return render_template_string(html_content)
if __name__== "__main__":
 app.run(debug=True,host="0.0.0.0", port = 5000) 