from flask import Blueprint,render_template,request,session,flash,current_app,url_for,redirect,send_file,after_this_request
from app.max.productroute import fun,kio
import time
from markupsafe import Markup
from app.all_dir.diretre12 import Static,template
from app.ismobile12 import is_mobile
import os
product = Blueprint("product",__name__,static_folder=Static,template_folder=template)

def sleep():
    print("Here process is finesed")
    time.sleep(2)


@product.route('/product',methods=['GET','POST'])
def product_page():
    if request.method == "POST":
        if session['last_upload']:
            # flash("Your image is in process to create string art")
            output = fun()
            path = url_for('static',filename=f"output/{output}")
            session['op'] = path
            if session.get('user_id'):
                kio(f"output/{output}")
            sleep()
            flash('DOM','ko')
            flash(Markup(f'your string art is ready. Download your image <a href ="{url_for("product.product_image")}">Click Here</a>'),'report')
            flash(Markup(f'your string art is ready. Download result <a href ="{url_for("product.product_report")}">Click Here</a>'),'report')
            return redirect(url_for('product.product_page'))
        else:
            flash("No uploaded pic. ",'error')
            return redirect(url_for('product.product_page'))
    data = session.get("user_data",{})   
    if is_mobile():
        return render_template('mobile/product.html',data=data)
    else:
        return render_template('pc/product.html',data=data)
    

@product.route('/dwreport',methods=['GET'])
def product_report():
    file_path = current_app.config.get('report')
    if not file_path:
        flash("Somthing went wrong in product_report route or image",'error')
        return redirect(url_for('product.product_page'))
    try:
        return send_file(file_path, as_attachment=True,download_name=f"user_report{session.get("user_id")}.txt")
    except FileNotFoundError:
        flash("file not found","error")
        return redirect(url_for('product.product_page')) 
         


@product.route('/dwimage', methods=['GET'])
def product_image():
    # Get base static folder path
    static_base = current_app.config.get('Size')

    # session['op'] example: '/static/output/out83efac9c-45d8-472a-bd28-23f69875dfb3.png'
    relative_path = session.get("op")

    if not relative_path:
        flash("Something went wrong in product_image route or image", 'error')
        return redirect(url_for('product.product_page'))

    # Remove leading /static/ if present
    if relative_path.startswith("/static/"):
        relative_path = relative_path[len("/static/"):]

    # Join full filesystem path
    image_path = os.path.join(static_base, relative_path)
    print("Full path:", image_path)

    if not os.path.exists(image_path):
        flash("File not found", "error")
        return redirect(url_for('product.product_page'))

    try:
        return send_file(
            image_path,
            as_attachment=True,
            download_name=f"user_image_{session.get('op')}"
        )
    except Exception as e:
        flash(f"Error sending file: {e}", "error")
        return redirect(url_for('product.product_page'))
