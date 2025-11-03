from flask import Blueprint,render_template
from app.all_dir.diretre12 import Static,template

home = Blueprint("home",__name__,static_folder=Static,template_folder=template)

@home.route('/',methods=['GET'])
def home_page():
    return render_template('home.html')

