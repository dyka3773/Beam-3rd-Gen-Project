from cProfile import label
import io
import numpy as np
import matplotlib
import asyncio

from matplotlib import pyplot as plt

from .utils import base64_util
from .status import get_temperature

matplotlib.use('agg')


FIGURES = ["temperature", "pressure"]


async def get_temp_plot(img: io.BytesIO) -> None:
    """Creates a matplotlib plot and stores it in the given io buffer.

    Args:
        img (io.BytesIO): A buffer to store the plot as an image.
    """
    time_range_of_plot = 60  # This value determines the time range of the plot

    sensor1, sensor2, sensor3 = await asyncio.gather(
        get_temperature("sensor1", time_range_of_plot),
        get_temperature("sensor2", time_range_of_plot),
        get_temperature("sensor3", time_range_of_plot)
    )

    # FIXME: This can probably be done in one line for every sensor so that we don't have to repeat the code
    x_1 = [i/3 for i in range(len(sensor1))]
    x_2 = [i/3 for i in range(len(sensor2))]
    x_3 = [i/3 for i in range(len(sensor3))]

    figure, ax = plt.subplots()

    ax.plot(x_1, sensor1, label="Sensor 1")
    ax.plot(x_2, sensor2, label="Sensor 2")
    ax.plot(x_3, sensor3, label="Sensor 3")
    ax.set_title("Temperature Plot")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (C)")
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
