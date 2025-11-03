from flask import Flask,render_template
from app.modules.auth import auth
from app.modules.about import about
from app.modules.dash import dash
from app.modules.home import home
from app.modules.product import product
from app.modules.regi import regi
from app.modules.test import test
from app.modules.upload import upload
from app.modules.errorhad import register_global_handlers
from app.modules.history import history
from app.modules.error12 import error12
# from app.extension import socketio
from flask import session
import os
from dotenv import load_dotenv
# import importlib
# moduless=['dash','about','home','product','test','regi','upload']

# blueprints=[]

# for i in moduless:
#     module = importlib.import_module(f'app.modules.{i}')
#     blueprint = getattr(module,i)
#     blueprints.append(blueprint)

load_dotenv()


def web():
    app = Flask(__name__)

    app.secret_key = os.getenv("SECRET_KEY")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # UPLOAD_FOLDER = 'static/uploads'
    app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR,'static','uploads')
    app.config['RESIZE'] = os.path.join(BASE_DIR,'static','resize')
    app.config['Size'] = os.path.join(BASE_DIR,'static')
    app.config['report'] = os.path.join(BASE_DIR,'thread','src','pathslastPath.txt')
    app.config['Edting_upload'] = os.path.join(BASE_DIR,'static','ed_upload')
    app.config['Edited_output'] = os.path.join(BASE_DIR,'static','ed_output')
    # app.config['output']= os.path.join(BASE_DIR,'static')
    app.register_blueprint(auth,url_prefix="")
    app.register_blueprint(dash,url_prefix="")
    app.register_blueprint(about,url_prefix="")
    app.register_blueprint(home,url_prefix="")
    app.register_blueprint(product,url_prefix="")
    app.register_blueprint(test,url_prefix="")
    app.register_blueprint(regi,url_prefix="")
    app.register_blueprint(upload,url_prefix="")
    app.register_blueprint(history,url_prefix="")
    app.register_blueprint(error12,url_prefix="")
    
    # app.register_blueprint(errorhad,url_prefix="")
    register_global_handlers(app)
    # socketio.init_app(app)
    return app



