from flask import Flask

app = Flask(__name__)

app.config.update(dict(
    DEBUG = True
))

app.route('/')
def index():
    return "Hello World!"

if __name__ = "__main__":
    app.run()
