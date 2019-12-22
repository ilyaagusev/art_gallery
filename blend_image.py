from PIL import Image


def blend_image(first_image, second_image, clarity):
    blended_image = Image.blend(first_image, second_image, clarity)
    return blended_image
