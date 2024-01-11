from flask import Flask, render_template, request
from functools import cache
from threading import Thread
from typing import Mapping, Tuple
import asyncio

from controllers import home_page, downlink_page, figures as figs, status as experiment_status
from telecoms import rxsm_receiver


app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index() -> str:
    return home_page.render()


@app.route('/downlink/')
def downlink() -> str:
    return downlink_page.render()


# The following routes are for special purposes and do not serve any pages

@app.route('/figures/<figure_name>')
async def figures(figure_name: str) -> tuple[str, int] | str:
    """Sends an image to the client.

    Args:
        figure_name (str): The name of the figure to be sent.

    Returns:
        Returns a tuple containing the image and the HTTP status code.
    """
    if figure_name in figs.FIGURES:
        return await figs.get_plot_by_type(figure_name)
    else:
        app.logger.error(
            f"Figure not found. The requested figure name was: {figure_name}")
        return "Figure not found", 400


@app.get('/status/')
async def status() -> Tuple[Mapping[str, str | int | None], int]:
    """Gets the status of the system.

    Returns:
        Returns a tuple containing the status and the HTTP status code.
    """

    motor_speed, sound_card_status, camera_status, LO, SOE, SODS, error_code = await asyncio.gather(
        experiment_status.get_motor_speed(),
        experiment_status.get_sound_card_status(),
        experiment_status.get_camera_status(),
        experiment_status.get_LO_signal(),
        experiment_status.get_SOE_signal(),
        experiment_status.get_SODS_signal(),
        experiment_status.get_errors()
    )

    status = {
        'motor_speed': motor_speed,
        'sound_card_status': sound_card_status,
        'camera_status': camera_status,
        'LO_status': LO,
        'SOE_status': SOE,
        'SODS_status': SODS,
        'errors': error_code
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
    return render_template('404.j2'), 404


# The following route is for favicon
@cache
@app.route('/favicon.ico')
def favicon():
    """Sends the favicon to the client.

    Returns:
        Returns the favicon image.
    """
    return app.send_static_file('img/favicon.png')


# Start the receiver thread
receiver_thread = Thread(
    target=rxsm_receiver.receive_data,
    daemon=True
)
receiver_thread.start()

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",  # This will make the app available to other computers on the network
        port=8000
    )
