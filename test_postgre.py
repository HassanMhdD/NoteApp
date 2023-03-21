#from flask import Flask
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, func,create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
from sqlalchemy_utils import database_exists, create_database
#from sqlalchemy_utils import database_exists, create_database
#from flask_sqlalchemy import SQLAlchemy 
from config import postgresql as settings

Base = declarative_base()
url= 'postgresql://postgres:hassan@localhost:5432/Employee'
engine = create_engine('postgresql://postgres:hassan@localhost:5432/Employee', echo=True)
Session = sessionmaker()

class Note(Base):
    __tablename__= 'Note'
    id = Column(Integer, primary_key=True)
    data = Column(String(10000))
    date = Column(DateTime(timezone=True), default=func.now()) #func_now() = current date and time 
    user_id = Column(Integer,ForeignKey('Users.id'))

class User(Base):
    __tablename__= 'Users'
    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True) # No user can have the same email than another user
    password = Column(String(150))
    first_name =Column(String(150))
    notes = relationship('Note') 

#def get_engine(username,pwd,hostname,port,db):
#    url = f'postgresql://{username}:{pwd}@{hostname}:{port}/{db}'
#    if not database_exists(url):
#        create_database(url)
#    engine = create_engine(url, pool_size=50, echo=False)
#    return engine
#
#
#def get_engine_from_settings():
#    keys = ['username','pwd','hostname','port_id','database']
#    if not all(key in keys for key in settings.keys()): #for every key in keys make sure they exists in settings
#        raise Exception('Bad config file') #if they don't raise an exception
#
#    return get_engine(settings['username'],
#                    settings['pwd'],
#                    settings['hostname'], 
#                    settings['port_id'], 
#                    settings['database'])
#eng_set= get_engine_from_settings()
#engine = create_engine(f'{eng_set.url}', echo=True)
#Session = sessionmaker()


#   if not database_exists(url):
#       Base.metadata.create_all(engine)
#   else:
#       print('Already Exist')

#al_session = Session(bind=engine)
#
#_user = User(id=1, email='test@gmail.com', first_name='test')
#
#al_session.add(new_user)
#al_session.commit()


#from sqlalchemy import text  

#from sqlalchemy import MetaData
#from sqlalchemy import Table, Column, Integer, String
#
#
#metadata_obj = MetaData()
#engine = create_engine('postgresql://postgres:hassan@localhost:5432/Employee', echo=True)
#
#user_table = Table(
#     "user_account",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(30)),
#     Column("fullname", String),
#)
#
#metadata_obj.create_all(engine)


#with engine.connect() as conn:
#    conn.execute(text("CREATE TABLE IF NOT EXISTS test (id int, y int)"))
#    conn.execute(
#        text("INSERT INTO test (id, y) VALUES (:id, :y)"),
#        [{"id": 1, "y": 1}, {"id": 2, "y": 4}],
#    )
#    conn.commit()
#db = SQLAlchemy()

#from sqlalchemy.sql import func


#class Note(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    data = db.Column(db.String(10000))
#    date = db.Column(db.DateTime(timezone=True), default=func.now()) #func_now() = current date and time 
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String(150), unique=True) # No user can have the same email than another user
#    password = db.Column(db.String(150))
#    first_name = db.Column(db.String(150))
#    notes = db.relationship('Note') 


#def get_engine(username,pwd,hostname,port,db):
#    url = f'postgresql://{username}:{pwd}@{hostname}:{port}/{db}'
#    if not database_exists(url):
#        create_database(url)
#    engine = create_engine(url, pool_size=50, echo=False)
#    return engine
#
#
#def get_engine_from_settings():
#    keys = ['username','pwd','hostname','port_id','database']
#    if not all(key in keys for key in settings.keys()): #for every key in keys make sure they exists in settings
#        raise Exception('Bad config file') #if they don't raise an exception
#
#    return get_engine(settings['username'],
#                    settings['pwd'],
#                    settings['hostname'], 
#                    settings['port_id'], 
#                    settings['database'])
#
#
#def get_session():
#    engine = get_engine_from_settings()
#    session = sessionmaker(bind=engine) ()
#    return session
#
#
#
#session = get_session()
#
#engine = get_engine_from_settings()
#print(engine.url)
#app2 = Flask(__name__) # App initialization
#app2.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_NAME_URL}'
#db.init_app(app2) #initialize database with the flask app
#
#
#db.init_app(app2) #initialize database with the flask app
#with app2.app_context():
#    db.create_all()

#user = User(id=1,email='hassan@gmail.com',password='123456', first_name='hassan')

#db.session.add(user)
#db.session.commit()