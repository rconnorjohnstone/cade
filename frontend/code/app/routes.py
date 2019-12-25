"""/app/routes.py [Frontend]

Description: Defines views for frontend app
Project: CadeSite
Author: Connor Johnstone
Date: 12/21/2019

"""
#=== Start import ===# 
# third party 
from flask import render_template, request, redirect, url_for

# std library
import requests
import logging
import re
import time
#=== End import ===# 

l = logging.getLogger(__name__)

def landing_page(): 
    if request.method == "GET":
        return render_template("landing.html"), 200

    if request.method == "POST": 
        try: 
            msg = request.form['message']
            return redirect(url_for('display_page', msg=msg))

        except Exception as e: 
            l.error("Error with front end landing page | {}".format(str(e)))
            return 500

def display_page():
    try:
        msg = request.args.get("msg")

        if not msg: 
            return "No Message Provided", 400

        api_res = requests.get('http://api:5000/', params={"msg":msg })
        api_data = api_res.json()['data']

        return render_template("display.html", 
            msg=api_data['msg']
            )

    except Exception as e:
        l.error("Error with front end display page | {}".format(str(e)))

        return 500
