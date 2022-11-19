# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:08:19 2022

@author: FRAUD
"""
from flask import Flask, render_template, redirect, url_for, request
app= Flask(__name__)

@app.route('/')
def home():
    return render_template(login.html) 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' %name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('login.html',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
if __name__ == '__main__':
   app.run(debug = True)     


