from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from config.settings import IMAGE_SIZE_LIMIT


def image_size_validator(file):
    """ File size validator
    :param file: file
    :param size_limit: file size limit in MB
    """
    if file.size > IMAGE_SIZE_LIMIT * 1024 ** 2:
        raise ValidationError(f"Max file size is {IMAGE_SIZE_LIMIT} Mb")


def get_image_html(img, width=50) -> str:
    """ Getting image in admin panel
    :param img: image file
    :param width: image width
    :return: image tag
    """
    return mark_safe(f"<img src='{img.url}' width={width}>") if img else "No image"