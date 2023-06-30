import base64

def encode_image(image):
    """Encodes image to base64 string.

    Args:
        image (Image): Image to be encoded.

    Returns:
        str: Base64 encoded image.
    """
    return base64.b64encode(image).decode()