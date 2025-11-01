from flask import Blueprint,render_template,session,request,url_for,redirect,flash
from app.database import get_cursor
auth = Blueprint("auth",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")

@auth.route('/auth',methods=['GET','POST'])
def auth_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = get_cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s && password = %s",(username,password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['user_id'] = user['id']
            return redirect(url_for('home.home_page'))
        else:
            flash("incorrect password or username",'error')
            return render_template('auth.html')
    return render_template('auth.html')

@auth.route('/logout',methods=['GET','POST'])
def logout():
    session.clear()
    flash('success fully log out')
    return redirect(url_for('dash.dash_page'))