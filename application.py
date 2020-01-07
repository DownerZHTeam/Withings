# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:20:18 2019

@author: S.Senapati
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><center>User authorization successful for the Withings Fatigue Management Trial at Downer</center></h1><p>Please use the state and code for generating access token</p> "
