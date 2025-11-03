from flask import Blueprint,request,current_app,session,url_for,flash,redirect
from app.allow.alowed_files import allowed_file
from app.max.uploadrooute import ok
from app.all_dir.diretre12 import Static,template

upload = Blueprint("upload",__name__,static_folder=Static,template_folder=template)




@upload.route('/upload',methods=['POST'])
def upload_pip():
    if 'image' not in request.files:
        flash("Somthing is wrong",'error')
        return redirect(url_for('product.product_page'))
    file  = request.files['image']
    if file.filename == '':
        flash("Somthing is wrong",'error')    
        return redirect(url_for('product.product_page'))
    if file and allowed_file(file.filename):
        ok(file)
        return redirect(url_for('product.product_page'))
    flash("File type not allowed", "error")
    return redirect(url_for('product.product_page'))

@upload.route('/uploadpins',methods=['POST'])
def uploadpins():
        session['user_data'] = {
        'pins': request.form['pin'],
        'liwt': request.form['liwt'],
        'mxli': request.form['mxli']
        }
        flash("This feture is not avalable ")
        return redirect(url_for('product.product_page'))
