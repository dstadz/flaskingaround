from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd2c736362984d2591ea5d5669693b752'

posts = [
    {
    'author': "alice",
    'title': "post 1",
    'content': 'first post',
    'date': '3/25/19'
    },  {
    'author': "bob",
    'title': "post 2",
    'content': 'second post',
    'date': '3/26/19'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)



@app.route('/about')
def about():
    return render_template('about.html', title='about')



@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form='form')
    
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form='form')


if __name__== '__main_':
    app.run(debug=True)
