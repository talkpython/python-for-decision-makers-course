import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    data = ['a', 'b', 'e', 'j']
    return flask.render_template('index.html', values=data)


if __name__ == '__main__':
    app.run(debug=True)
