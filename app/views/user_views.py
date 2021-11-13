from flask import (
    Blueprint,
    render_template,
    url_for,
    abort,
    g,
)

from app import db
from app.models import User

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/')
def user_list():
    users = User.query.all()
    return render_template('user/list.html', user_list=users)

@bp.route('/<user_id>/')
def user_info(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user/info.html', user=user)

# /user/ 이하 페이지는 전부 로그인 후 접근 가능 
@bp.before_request
def load_logged_in_user():
    if g.user is None:
        abort(404)
    