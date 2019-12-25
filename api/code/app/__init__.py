"""/app/__init__.py

Description: App factory for api service
Project: CadeSite
Author: Connor Johnstone
Date: 12/21/2019

"""
#=== Start imports ===# 

# std lib 
import logging

# third party
from flask import Flask 
import redis

# local 
from .routes import message_service

#=== End imports ===# 

# Define Routes 
ROUTE_TABLE = {
    '/': message_service,
}

# Set up configuration data 
class Config: 
    REDIS_DB = redis.Redis(host='redis', port=6379)

def new_app(): 
    """ Creates a new flask app instance 
    """
    app = Flask(__name__) 

    # add config data 
    app.config.from_object(Config())

    # Construct Routes
    for url in ROUTE_TABLE:
        app.add_url_rule(url, view_func=ROUTE_TABLE[url])

    return app

