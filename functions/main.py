# Welcome to Cloud Functions for Firebase for Python!
# To learn more, see https://firebase.google.com/docs/functions

from firebase_functions import https_fn
from firebase_admin import initialize_app
import sys
import os

# Initialize firebase admin
initialize_app()

# Import the Flask application
from app import app as flask_app

# Expose Flask app as a single Cloud Function
@https_fn.on_request()
def predict_laptop(req: https_fn.Request) -> https_fn.Response:
    with flask_app.request_context(req.environ):
        return flask_app.full_dispatch_request()
