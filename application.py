# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:20:18 2019

@author: S.Senapati
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><center><u>Welcome to Downer Withings Fatigue Management Trial</u></center></h1>"
