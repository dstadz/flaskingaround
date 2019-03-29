from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = 'd2c736362984d2591ea5d5669693b752'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)



from blog import routes