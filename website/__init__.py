from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Changer pour PostgreSQL  
from os import path
from flask_login import LoginManager 
#from test_postgre import get_engine_from_settings
from test_postgre import engine, Session
#from .models import locale_session

db = SQLAlchemy()
#DB_NAME = "database.db"


locale_session = Session(bind=engine)
url= 'postgresql://postgres:hassan@localhost:5432/Employee'

def create_app():
    app = Flask(__name__) # App initialization
    app.config['SECRET_KEY'] = 'secretkey' # Encrypt or secure the cookies and session data related to the website (DON'T STORE IT IN PLAIN TEXT)
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #SQLalchemy Database is stored at this location
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{url}'
    db.init_app(app) #initialize database with the flask app
    #db = SQLAlchemy(app)



    from .views import views # import the Blueprint
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()
    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #Where should flash redirect if user is not logged in and login is required
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    return app

#def create_database(app):
#    if not path.exists('website/' + DB_NAME ):
#        db.create_all(app=app)
#        print('Created Database.')
