from flask import Blueprint,render_template,request,session,flash

errorhad = Blueprint("errorhad",__name__,static_folder="/home/shoarya/Desktop/web/app/static",template_folder="/home/shoarya/Desktop/web/app/templates")

def register_global_handlers(app):
    @app.errorhandler(404)
    def global_404(e):
        return render_template("404.html"), 404
    @app.errorhandler(405)
    def global_405(e):
        return render_template("405.html"), 405
    @app.errorhandler(500)
    def global_500(e):
        return render_template("500.html"), 500
    @app.errorhandler(400)
    def global_400(e):
        return render_template("400.html"), 400