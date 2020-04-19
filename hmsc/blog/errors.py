from flask import render_template
from blog import app
# 错误处理函数
@app.errorhandler(404)
def not_found(e):
    
    return render_template('errors/404.html'),404