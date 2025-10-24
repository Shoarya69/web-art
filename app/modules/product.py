from flask import Blueprint,render_template,request,session,flash,current_app,url_for,redirect,send_file
from app.max.productroute import fun
import time
from markupsafe import Markup

product = Blueprint("product",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")

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
            sleep()
            flash('DOM','ko')
            flash(Markup(f'your string art is ready. Download result <a href ="{url_for("product.product_report")}">Click Here</a>'),'report')
            return render_template('product.html')
        else:
            flash("No uploaded pic. ",'error')
            return render_template('product.html')
        
    return render_template('product.html')

@product.route('/report',methods=['GET'])
def product_report():
    file_path = current_app.config.get('report')
    if not file_path:
        flash("Somthing went wrong in product_report route",'error')
        return redirect(url_for('product.product_page'))
    try:
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return "File not found!", 404
         





