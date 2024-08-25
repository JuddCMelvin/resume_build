from flask import (Blueprint, render_template)

bp = Blueprint('project', __name__, url_prefix="/projects")

@bp.route('/')
def index(): 
    return render_template('index.html')