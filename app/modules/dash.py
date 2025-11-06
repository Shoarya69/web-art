from flask import Blueprint,render_template,session
from app.all_dir.diretre12 import Static,template

dash = Blueprint("dash",__name__,static_folder=Static,template_folder=template)

@dash.route('/dashboard',methods=['GET','POST'])
def dash_page():
    return render_template("pc/dashboard.html")