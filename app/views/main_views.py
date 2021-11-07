from flask import (
    Blueprint,
    render_template,
)

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def main():
    # return 'main'
    return render_template('index.html')

@bp.route('/member_list')
def member_list():
    return 'Member List'

@bp.route('/mypage')
def mypage():
    return 'Mypage'
