from flask import Flask, render_template,url_for, flash , redirect
##from flask_sqlalchemy import SQLAlchemy 
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='8d9470cdab48053150f37b7cf538fa53'

posts=[{
    'Author':'Amish',
    'Title':'Secrets of naggas',
    'Content':'Contents of secrets of naggas is not available at this time',
    'Date':'25/01/2020'
    },
    {
    'Author':'ABC',
    'Title':'XYX',
    'Content':'Contents of XYZ is not available at this time',
    'Date':'26/01/2020'
    }
]

@app.route('/')
@app.route('/home')
def Home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('Home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)


if __name__ == '__main__':
    app.run(debug=True)
