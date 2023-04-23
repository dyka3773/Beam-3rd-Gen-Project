import io
import numpy as np
import matplotlib

from matplotlib import pyplot as plt

from .utils import base64_util

matplotlib.use('agg')

def get_plot(img: io.BytesIO) -> None:
    """Creates a matplotlib plot and stores it in the given io buffer.

    Args:
        img (io.BytesIO): A buffer to store the plot as an image.
    """
    y = [np.random.randint(0,100) for i in range(50)]
    x = [i for i in range(50)]
    
    figure, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_title("Test Figure")
    ax.set_xlabel("Eirini")
    ax.set_ylabel("Iraklis")
    ax.grid()
    figure.savefig(img, format='png')
    plt.close(figure)


def render_plot() -> str:
    """Renders a plot into an HTML image tag by encoding it to base64.
    
    Returns:
        str: HTML image tag.
    """
    img = io.BytesIO()
    get_plot(img)
    img.seek(0)
    
    encoded_image = base64_util.encode_image(img.getvalue())
    
    return f"{encoded_image}"