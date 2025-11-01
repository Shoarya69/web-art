from flask import Blueprint,render_template,request,flash,session
from app.editing.image_12 import editing
from app.allow.alowed_files import allowed_file
from app.max.testroute import gog,gog2
import time
test = Blueprint("test",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")


@test.route('/test',methods = ['GET','POST'])
def test_page():
    form_data = {}
    if  request.method == 'POST':
        option = request.form['edit_type']
        image = request.files['ed_image']
        if not option:
            flash("Plese kindly select your edit type","error")
            return render_template("test.html")
        form_data['option'] = option
        if not image:
            flash("Please kindly select your image for editing","error")
            return render_template("test.html")
        if image.filename and allowed_file(image.filename):
            gog(image)
            output = editing(option,session.get('ed_route'))
            time.sleep(2)
            if session.get('user_id'):
                gog2(output)
            session['ed_output_ed'] = f"/ed_output/{output}"
            flash("File uploaded Sucessfully",'sucess')
            return render_template('test.html',data=form_data)
        else:
            flash("This file is not in allowed extenstion","error")
            return render_template('test.html',data = form_data)        
    return render_template('test.html',data = form_data)