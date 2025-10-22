from flask import Blueprint,render_template,session

dash = Blueprint("dash",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")

@dash.route('/dashboard',methods=['GET','POST'])
def dash_page():
    return render_template("dashboard.html")