# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: Anais Lawson
anl2140
run three pages: index.html , plan.html, music.html
index.html is the home page and has my picture and info as well as links to the
other two pages and the link to a website I like to go to
plan.html describes what my plans for the upcoming summer are
music.html describes what are my top 5 favorite songs right now
There is also a link to my favorite podcast  
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/plan")
def plans():
    return render_template("plan.html")
@app.route("/music")
def fav():
    return render_template("music.html")


#start the server
if __name__ == "__main__":
    app.run()