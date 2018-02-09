from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config.update(dict(
    DEBUG = True
))

@app.route('/')
def index():
    return render_template('index.html', json=posts.get_list_post())

@app.route('/about')
def about():
    return render_template('about.html')


app.errorhandler(404)
def error404(error):
    return render_template('error.html'), 404


if __name__ = "__main__":
    app.run()
