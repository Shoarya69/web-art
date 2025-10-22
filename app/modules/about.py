from flask import Blueprint,render_template

about = Blueprint("about",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")

@about.route('/about',methods=['GET'])
def about_page():
    return render_template('about.html')