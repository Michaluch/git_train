from flask import Flask

app = Flask(__name__)

app.config.update(dict(
    DEBUG = True
))

app.route('/')
def index():
    """This Method run web app""
    return "Hello World!"

if __name__ = "__main__":
    app.run()
