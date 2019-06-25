#!/usr/bin/python3
import logging
import sys
# logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/web/Flask/bokeh_stock_ticker/')
#
from script import app as application
application.secret_key = 'ddNwrIQWJz1xBP8Wqi2ZWZs2KDfEKjYo9hrD7bJodk4'

if __name__ == "__main__":
    app.run()
