from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__== '__main_':
    app.run(debug=True)
