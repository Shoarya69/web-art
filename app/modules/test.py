from flask import Blueprint,render_template,request,flash,session,redirect,url_for
from app.editing.image_12 import editing
from app.allow.alowed_files import allowed_file
from app.max.testroute import gog,gog2
import time
from app.all_dir.diretre12 import Static,template
from app.ismobile12 import is_mobile

test = Blueprint("test",__name__,static_folder=Static,template_folder=template)


@test.route('/test',methods = ['GET','POST'])
def test_page():
    form_data = {}
    if request.method == 'GET':
        form_data['option'] = request.args.get('option')
        if is_mobile():
            return render_template('mobile/test.html',data = form_data)
        else:
            return render_template('pc/test.html',data = form_data)
    if  request.method == 'POST':
        option = request.form['edit_type']
        image = request.files['ed_image']
        if not option:
            flash("Plese kindly select your edit type","error")
            return redirect(url_for('test.test_page'))
        form_data['option'] = option
        if not image:
            flash("Please kindly select your image for editing","error")
            return redirect(url_for('test.test_page'))
        if image.filename and allowed_file(image.filename):
            gog(image)
            if session.get('ed_route'):
                output = editing(option,session.get('ed_route'))
            else:
                flash("somthing went wrong in backend of edting route")
                return redirect(url_for('test.test_page'))
            time.sleep(2)
            if session.get('user_id'):
                gog2(output)
            session['ed_output_ed'] = f"/ed_output/{output}"
            flash("File uploaded Sucessfully",'success')
            return redirect(url_for('test.test_page',data=form_data))
            # return render_template('test.html',data=form_data)
        else:
            flash("This file is not in allowed extenstion","error")
            return redirect(url_for('test.test_page',data=form_data))   
   