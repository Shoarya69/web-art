from flask import Blueprint,render_template
from app.all_dir.diretre12 import Static,template

about = Blueprint("about",__name__,static_folder=Static,template_folder=template)

@about.route('/about',methods=['GET'])
def about_page():
    return render_template('about.html')