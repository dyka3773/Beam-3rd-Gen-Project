import io
import matplotlib
import asyncio
import logging

from matplotlib import pyplot as plt

from .utils import base64_util
from .status import get_temperature

matplotlib.use('agg')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

FIGURES = ["temperature", "pressure"]


async def get_temp_plot(img: io.BytesIO) -> None:
    """Creates a matplotlib plot and stores it in the given io buffer.

    Args:
        img (io.BytesIO): A buffer to store the plot as an image.
    """
    time_range_of_plot = 60  # This value determines the time range of the plot

    sensor1_data, sensor2_data, sensor3_data = await asyncio.gather(
        get_temperature("sensor1", time_range_of_plot),
        get_temperature("sensor2", time_range_of_plot),
        get_temperature("sensor3", time_range_of_plot)
    )

    figure, ax = plt.subplots()

    logging.debug(f"Sensor 1 data: {sensor1_data}")
    logging.debug(f"Sensor 2 data: {sensor2_data}")
    logging.debug(f"Sensor 3 data: {sensor3_data}")

    ax.plot(*sensor1_data, label="Sensor 1")
    ax.plot(*sensor2_data, label="Sensor 2")
    ax.plot(*sensor3_data, label="Sound Card")
    ax.set_title("Temperature Plot")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (C)")
    ax.legend()
    ax.grid()
    figure.savefig(img, format='png')
    plt.close(figure)


async def get_plot_by_type(type: str) -> str:
    """Returns a base64 encoded image of a matplotlib plot.

    Args:
        type (str): The type of plot to be returned. Available types are:
            - temperature
            - pressure

    Returns:
        str: A base64 encoded image of a matplotlib plot.
    """
    img = io.BytesIO()

    if type == "temperature":
        await get_temp_plot(img)
    else:
        raise ValueError("Invalid figure type")

    img.seek(0)

    encoded_image = base64_util.encode_image(img.getvalue())

    return f"{encoded_image}"
