import datetime
from flask import Flask, render_template, url_for

from controllers import home_page, downlink_page, uplink_page


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return home_page.render()

@app.route('/downlink/')
def downlink():
    return downlink_page.render()

@app.route('/uplink/')
def uplink():
    return uplink_page.render()

# TODO: Add pages for the test plans here

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(
        host="0.0.0.0", # This will make the app available to other computers on the network
        port="8000"
    )