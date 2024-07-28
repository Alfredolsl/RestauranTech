from app import app, db, login_manager
from app.forms import RegisterForm, LoginForm
from app.models.user import User
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html', logged_in=current_user.is_authenticated)

@app.route('/crm')
@login_required
def crm():
    user_info = {
        'id': current_user.user_id
    }
    return render_template('crm.html', user_info=user_info)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('crm'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        if not form.duplicate_email(email):
            name = form.name.data
            hashed_password = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)
            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('crm'))
        else:
            flash('Email already registered', 'danger')
    
    return render_template('register.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/inventory')
@login_required
def inventory():
    user_info = {
        'id': current_user.user_id
    }
    return render_template('crm.html', user_info=user_info)

@app.route('/costs')
@login_required
def costs():
    user_info = {
        'id': current_user.user_id
    }
    return render_template('crm.html', user_info=user_info)
