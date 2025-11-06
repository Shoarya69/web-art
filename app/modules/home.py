from flask import Blueprint,render_template
from app.all_dir.diretre12 import Static,template
from app.ismobile12 import is_mobile
home = Blueprint("home",__name__,static_folder=Static,template_folder=template)

@home.route('/',methods=['GET'])
def home_page():
    if is_mobile():
        return render_template('mobile/home.html')
    else:
        return render_template('pc/home.html')

