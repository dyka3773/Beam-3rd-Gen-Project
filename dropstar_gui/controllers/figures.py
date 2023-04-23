import io
import numpy as np
import matplotlib

from matplotlib import pyplot as plt

from .utils import base64_util

matplotlib.use('agg')

FIGURES = ["temperature", "pressure"]

def get_temp_plot(img: io.BytesIO) -> None:
    """Creates a matplotlib plot and stores it in the given io buffer.

    Args:
        img (io.BytesIO): A buffer to store the plot as an image.
    """
    fake_time = 100
    y = [np.random.randint(-50,100) for _ in range(fake_time)]
    x = [i for i in range(fake_time)]
    
    figure, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_title("Temperature Plot")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (C)")
    ax.grid()
    figure.savefig(img, format='png')
    plt.close(figure)

def get_pressure_plot(img: io.BytesIO) -> None:
    """Creates a matplotlib plot and stores it in the given io buffer.
    
    Args:
        img (io.BytesIO): A buffer to store the plot as an image.
    """
    fake_time = 100
    y = [np.random.randint(8,32)/16 for _ in range(fake_time)]
    x = [i for i in range(fake_time)]
    
    figure, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_title("Pressure Plot")
    ax.set_xlabel("Time")
    ax.set_ylabel("Pressure (atm)")
    ax.grid()
    figure.savefig(img, format='png')
    plt.close(figure)

def get_plot_by_type(type: str) -> str:
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
        get_temp_plot(img)
    elif type == "pressure":
        get_pressure_plot(img)
    else:
        raise ValueError("Invalid figure type")
    
    img.seek(0)
    
    encoded_image = base64_util.encode_image(img.getvalue())
    
    return f"{encoded_image}"
