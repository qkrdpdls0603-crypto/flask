from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello pybo!'

@bp.route('/hello')
def hello_world():
    return 'Hello pybo!'

@bp.route('/about')
def about():
    return 'About pybo!'

@bp.route('/contact')
def contact():
    return 'Contact pybo!'

@bp.route('/bye')
def bye_world():
    return 'Bye pybo!'