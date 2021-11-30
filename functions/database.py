from flask_sqlalchemy import SQLAlchemy
from flask import  Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask (__name__)
engine = create_engine('postgresql://harkwrvfhctglg:04ec0331c282b55287482b65d59090923dce0d82e515f70a51cc45096d6010d6@ec2-34-196-34-142.compute-1.amazonaws.com:5432/d7oqck16jou484')
db = scoped_session(sessionmaker(bind=engine))


