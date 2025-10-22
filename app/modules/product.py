from flask import Blueprint,render_template,request,session,flash,current_app,url_for,redirect
from app.max.productroute import fun
import time

product = Blueprint("product",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")

def sleep():
    print("Here process is finesed")
    time.sleep(2)


@product.route('/product',methods=['GET','POST'])
def product_page():
    if request.method == "POST":
        if session['last_upload']:
            output = fun()
            path = url_for('static',filename=f"output/{output}")
            session['op'] = path
            sleep()
            flash('DOM','ko')
            flash('your string art is ready','sucess')
            return render_template('product.html')
        else:
            flash("No uploaded pic. ",'error')
            return render_template('product.html')
        
    return render_template('product.html')




