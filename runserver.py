from flask import Flask

app = Flask(__name__)

app.config.update(dict(
    DEBUG = False
))

app.route('/')
def index():
    return "Hello World!"

app.errorhandler(404)
def error404(error):
    return render_template('error.html'), 404


if __name__ = "__main__":
    app.run()
