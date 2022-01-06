CONNECTION AND SETTING UP THE DATABASE 
======================================
#database.py 
---------------------------------------------------------------
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
path = os.path.dirname(__file__)

engine = create_engine('sqlite:////{}/luckydraw.db'.format(path))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)
    print('We are connected to database successfully')
    
#app.py 
-------
@app.before_first_request
def init():
    init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

CREATING MODELS 
===============
#models/restaurants.py 
----------------------
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime
import uuid
import datetime
from database import Base

class Restaurants(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(200), nullable=True)
    site_url = Column(String(100), nullable = True)
    draw = Column(Integer(), default= 0)
    created_time = Column(DateTime(), nullable=False)
    modified_time = Column(DateTime(), nullable= False)

    def __init__(self, name, description, site_url):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.site_url = site_url
        self.created_time = datetime.datetime.now()


    def __repr__(self):
        return f'<Restaurant {self.name!r}>'
---------------------------------------------------------

