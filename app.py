# -*- coding: utf-8 -*-
"""
Created on Tue Mar  10 11:41:04 2021

@author: tj john
"""
from flask import Flask, request,render_template
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)

pickle_in = open("lr.pkl","rb")
predict_Rem_Ind=pickle.load(pickle_in)


@app.route('/')                        # fn for homepage
def welcome():
    return render_template("index.html")



if __name__=='__main__':
    app.run()
    