from flask import render_template,redirect,request,Flask,url_for,flash
from blog import db,app
from blog.models import User,Commodity
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user

# 首页
@app.route('/')
def index():

    commodity = Commodity.query.all()

    return render_template('index.html',comm=commodity)


# 登录
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password']

        if not username or not password:
            flash('输入错误')
            return redirect(url_for('login'))

        user = User.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('登录成功')
            return redirect(url_for('index'))
        flash('用户名或密码错误')
        return redirect(url_for('login'))
    return render_template('login.html')


# 登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('已退出')
    return redirect(url_for('index'))


# 设置
@app.route('/settings',methods=['GET','POST'])
@login_required
def settings():
    if request.method == 'POST':
        name= request.form['name']
        if not name or len(name) > 20:
            flash('输入错误')
            return redirect(url_for('settings'))
        current_user.name = name # 等同于下面
        # user = User.query.first()
        # user.name = name
        db.session.commit()
        flash('设置name成功')
        return redirect(url_for('index'))
    return render_template('settings.html')