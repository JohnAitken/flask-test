from flask import Flask

def create_app():
    app = Flask(__name__) #initialising flask
    app.config['SECRET_KEY'] = 'psst'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/') #registering the blueprints
    app.register_blueprint(auth, url_prefix='/')
    return app
    