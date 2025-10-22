from flask import Blueprint,render_template

test = Blueprint("test",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")


@test.route('/test')
def test_page():
    return render_template('test.html')