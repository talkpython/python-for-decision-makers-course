import flask

from guitary.services import catalog_service

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/guitars/<style>')
@app.route('/guitars')
def guitars(style=None):
    guitar_list = catalog_service.all_guitars(style)
    return flask.render_template('guitars.html', guitars=guitar_list)


if __name__ == '__main__':
    app.run(debug=True)
