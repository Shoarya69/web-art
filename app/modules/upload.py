from flask import Blueprint,request,current_app,session,url_for,flash,redirect

from app.max.uploadrooute import ok
upload = Blueprint("upload",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")

ALLOWED_EXTENSION={'png','jpg','jpeg','gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION



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
    flash("Please do not submit in  this session")
    return redirect(url_for('product.product_page'))