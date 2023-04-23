from flask import Flask, render_template, request, url_for

from controllers import home_page, downlink_page, uplink_page, test_figure


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

# TODO: Add pages for the test plans

@app.route('/figures/<figure_name>')
@app.route('/figures/<figure_name>/<int:code>')
def figures(figure_name: str, code: int = None):
    """Sends an image to the client.

    Args:
        figure_name (str): The name of the figure to be sent.
        code (int, optional): The code of the figure to be sent. Defaults to None.

    Returns:
        Returns a tuple containing the image and the HTTP status code.
    """
    app.logger.info(f"Figure name: {figure_name}")
    if code:
        app.logger.info(f"Code: {code}")
    
    # return test_figure.render(figure_name, code) # FIXME: This should be the way to do it
    return test_figure.render_plot()

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(f"Page not found. The requested URL was: {request.url}")
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(
        host="0.0.0.0", # This will make the app available to other computers on the network
        port="8000"
    )