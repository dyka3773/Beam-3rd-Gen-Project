from flask import Flask, render_template, request, url_for

from controllers import home_page, downlink_page, uplink_page, figures as figs, status as experiment_status


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

# The following routes are for special purposes and do not serve any pages

@app.route('/figures/<figure_name>')
def figures(figure_name: str):
    """Sends an image to the client.

    Args:
        figure_name (str): The name of the figure to be sent.

    Returns:
        Returns a tuple containing the image and the HTTP status code.
    """    
    # return figs.render(figure_name, code) # FIXME: This should be the way to do it
    if figure_name in figs.FIGURES:
        return figs.get_plot_by_type(figure_name)
    else:
        return "Figure not found", 400
    
@app.get('/status/')
def status():
    """Gets the status of the system.

    Returns:
        Returns a tuple containing the status and the HTTP status code.
    """
    status = {
        'motor_speed': experiment_status.get_motor_speed(),
        'sound_card_status': experiment_status.get_sound_card_status(),
        'camera_status': experiment_status.get_camera_status()
    }
    return status, 200

# The following routes are for error handling

@app.errorhandler(404)
def page_not_found(error):
    """Handles 404 errors.
    
    Args:
        error (Exception): The error that was raised.
    
    Returns:
        Returns a tuple containing the rendered 404 page and the HTTP status code.
    """
    app.logger.error(f"Page not found. The requested URL was: {request.url}")
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(
        host="0.0.0.0", # This will make the app available to other computers on the network
        port="8000"
    )