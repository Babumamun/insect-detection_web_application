#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 15:45:16 2022

@author: mac
"""
from  flask import Flask
app= Flask(__name__)
@app.route('/')
def hello_world():

    return static("/Users/mac/spyder/web/index.html")
app.run()