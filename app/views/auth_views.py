from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from app import db
from app.forms import UserCreateForm, UserSigninForm
from app.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        name=form.name.data,
                        email=form.email.data,
                        birth=form.birth.data,
                        )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.main'))
        else:
            flash('이미 존재하는 ID입니다.')

    return render_template('auth/signup.html', form=form)

@bp.route('/signin/', methods=('GET', 'POST'))
def signin():
    form = UserSigninForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.main'))
        flash(error)

    return render_template('auth/signin.html', form=form)

@bp.route('/signout/', methods=('GET',))
def signout():
    # session의 모든 값을 삭제
    session.clear()

    return redirect(url_for('main.main'))

# 라우트 함수보다 먼저 실행됨
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)