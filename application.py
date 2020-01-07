# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:20:18 2019

@author: S.Senapati
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
