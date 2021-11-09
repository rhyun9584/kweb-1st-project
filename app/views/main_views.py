from flask import (
    Blueprint,
    render_template,
)

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def main():
    # return 'main'
    return render_template('index.html')
    