import click
from blog import app,db
from blog.models import User,Movie


# 生成管理员账户
@app.cli.command()
@click.option('--username',prompt=True,help='用户名')
@click.option('--password',prompt=True,help='密码',confirmation_prompt=True,hide_input=True)
def admin(username,password):
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('更新用户')
        user.username = username
        user.set_password(password)  # 设置密码
    else:
        click.echo('创建用户')
        user = User(username=username,name='admin')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('完成')


# 自定义命令
@app.cli.command()  # 注册命令
@click.option('--drop', is_flag=True,help='先删除再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("数据库创建完成")

# 向数据库增加数据
@app.cli.command()
def forge():
    name = "user"
    movies = [
        {'title': '机械师', 'year':'2020'},
        {'title': '机械师2', 'year':'2020'},
        {'title': '速度与激情', 'year':'2008'},
        {'title': '速度与激情3', 'year':'2012'},
        {'title': '速度与激情8', 'year':'2020'},
    ]
    user = User(name=name)
    db.session.add(user)
    for i in movies:
        movie = Movie(title=i['title'],year=i['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo("添加数据完成")

