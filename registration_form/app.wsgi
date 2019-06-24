#!/usr/bin/python3
import logging
import sys
# logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/web/Flask/registration_form/')
#
from server import app as application
application.secret_key = 'anything you wish'

if __name__ == "__main__":
    app.run()
