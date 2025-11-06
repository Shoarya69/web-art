from flask import Blueprint,render_template,request,flash,session,redirect,url_for,current_app,send_file
from markupsafe import Markup
import os
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
            session.modified = True
            flash(Markup(f'Sucessfully Download <a href ="{url_for("test.test_image")}">Click Here</a>'),'report')
            return redirect(url_for('test.test_page',data=form_data))
            # return render_template('test.html',data=form_data)
        else:
            flash("This file is not in allowed extenstion","error")
            return redirect(url_for('test.test_page',data=form_data))   
   

@test.route('/dowimage', methods=['GET'])
def test_image():
    static_base = current_app.config.get('Size')
    relative_path = session.get("ed_output_ed")

    print("Session path:", relative_path)
    print("Static base:", static_base)

    if not relative_path:
        flash("Something went wrong — no image found in session", "error")
        return redirect(url_for('test.test_page'))

    # Normalize relative path
    relative_path = relative_path.strip("/")  # removes leading and trailing slashes
    # Make sure 'static' not duplicated
    if relative_path.startswith("static/"):
        relative_path = relative_path[len("static/"):]

    # Construct final absolute path
    image_path = os.path.join(static_base, relative_path)
    image_path = os.path.normpath(image_path)  # normalize the path

    print("Final resolved path:", image_path)

    if not os.path.exists(image_path):
        flash("File not found at expected location!", "error")
        return redirect(url_for('test.test_page'))

    try:
        return send_file(
            image_path,
            as_attachment=True,
            download_name=f"user_image_{session.get('ed_output_ed')}"
        )
    except Exception as e:
        flash(f"Error sending file: {e}", "error")
        return redirect(url_for('test.test_page'))
