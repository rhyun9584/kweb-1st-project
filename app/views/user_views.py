from flask import (
    Blueprint,
    render_template,
    url_for,
    abort,
    session,
    g,
)

from app import db
from app.models import User

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/')
def user_list():
    if g.user is None:
        # 로그인하지않은 경우 404 NOT FOUND
        abort(404)

    users = User.query.all()
    return render_template('user/list.html', user_list=users)

@bp.route('/<user_id>/')
def user_info(user_id):
    if g.user is None:
        # 로그인하지않은 경우 404 NOT FOUND
        abort(404)

    user = User.query.get_or_404(user_id)
    return render_template('user/info.html', user=user)
    