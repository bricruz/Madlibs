from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route('/form')
def show_form():
    choice = request.args['stories']
    return render_template("form.html", storychoice = choice)

@app.route('/story')
def show_story():
    choice = request.args['stories']
    story = stories[choice]
    madlib = story.generate(request.args)
    return render_template("story.html", madlib = madlib)
    

@app.route('/storyform')
def show_story_form():

    return render_template("storyform.html")

# story = Story([],'')
# stories = {'story1':'Way back in {place}, there lived a silly {adjective} {noun}. It would always {verb} {plural_noun}.', 'story2':'Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.', 'story3':"In west {place}, there resided a chill {adjective} {noun}. It never didn't {verb} {plural_noun}."}