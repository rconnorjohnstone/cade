"""/app/routes.py

Description: Route definition for api service
Project: CadeSite
Author: Connor Johnstone
Date: 12/21/2019

"""
#=== Start imports ===# 

# third party
from flask import current_app, jsonify, request

# std lib
import logging
import time
import re

#=== End imports ===# 

l = logging.getLogger(__name__)

def message_service(): 
    try:
        # get message and check if exists
        msg = request.args.get("msg")

        if not msg: 
            return jsonify(error=["Please provide a message"]), 400

        rkey = "msg_" + msg
        if not current_app.config["REDIS_DB"].exists(rkey):
            donut_msg = msg
        else: 
            donut_msg = current_app.config["REDIS_DB"].hget(rkey, "msg").decode('utf-8')

        data = {
            "metadata": { 
                "gen_at": time.strftime("%d %m, %H:%M:%S"),
                "input_msg": msg
            }, 
            "msg": donut_msg
        }

        l.info("successfully generated donut message")

        return jsonify(data=data), 200
    

    except Exception as e: 
        l.exception("An error occured in donut generation | {}".format(str(e)))

        return jsonify(error=["Could not return a donut filled message"]), 500
