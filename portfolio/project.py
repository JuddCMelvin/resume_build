from flask import Blueprint 

bp = Blueprint('project', __name__, url_prefix="/projects")

@bp.route('/')
def index(): 
    return 'this is the project page'