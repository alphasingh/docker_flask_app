from flask import Blueprint

others_bp = Blueprint('others', __name__)


@others_bp.route('/')
def hello():
    return {
            'status': 'OK', 
            'Blueprint': 'others_bp', 
            'created':'22 April 2022', 
            'updated':'11 MAY 2022', 
            'author':'Abhay'
            }
