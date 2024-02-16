from flask import Blueprint, Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

rate_limits_bp = Blueprint('rate_limits', __name__)
app = Flask(__name__)

"""
Rate limiting quickstart
https://flask-limiter.readthedocs.io/en/stable/
"""
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@rate_limits_bp.route('/slow')
@limiter.limit("1 per day")
def slow():
    return ":("


@rate_limits_bp.route("/medium")
@limiter.limit("1/second", override_defaults=False)
def medium():
    return ":|"


@rate_limits_bp.route("/fast")
def fast():
    return ":)"


@rate_limits_bp.route("/ping")
@limiter.exempt
def ping():
    return "PONG"
