from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
bootstrap = Bootstrap(app)

## before running, make sure to...
## . /bin/activate ## to enter venv  
## export FLASK_APP=main.py ## to set the FLASK_APP variable to this file
## export FLASK_ENV=development ## to set the environment to 'development'
## python -m flask run ## to run after setting venv and variables

class name_form(FlaskForm):
    name = StringField('Enter your name: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500_error.html"), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = name_form()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)



