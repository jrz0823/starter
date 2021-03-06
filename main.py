from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404