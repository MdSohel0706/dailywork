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

