from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story 

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/story')
def show_story():
    madlib = story.generate(request.args)
    return render_template("story.html", madlib = madlib)