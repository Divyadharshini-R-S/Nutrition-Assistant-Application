# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:40:29 2022

@author: admin
"""

from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route("/")
def home():
    #api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    #api_url = 'https://api.spoonacular.com/recipes/guessNutrition?title='
    #query = 'Dosa'
    #response = requests.get(api_url + query, headers={'X-Api-Key': '8f123f2f983b4b69bfe1e4a25f7bfb06'})
    #if response.status_code == requests.codes.ok:
    #    print(response.text)
    #else:
    #    print("Error:", response.status_code, response.text)
    return render_template("History.html")

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method=="POST":
        username=request.form.get('username')
        email=request.form.get('email')
        phone=request.form.get('phone')
        return render_template("home.html",username=username,email=email,phone=phone)

@app.route("/support")
def support():
    return render_template("support.html")

if __name__ == '__main__':
    app.run(debug=True)