from flask import Blueprint,render_template

home = Blueprint("home",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")

@home.route('/',methods=['GET'])
def home_page():
    return render_template('home.html')

