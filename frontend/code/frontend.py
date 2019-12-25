"""/frontend.py [Frontend]

Description: Entrypoint for frontend service
Project: Cade's Site
Author: Connor Johnstone
Date: 12/21/2019

"""
#=== Start imports ===# 

# third party
from waitress import serve

# local 
from app import new_app

#=== End imports ===# 

if __name__ == "__main__":
    app = new_app()
    serve(app, host="0.0.0.0", port=5000)
