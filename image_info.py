from PIL import Image


def image_information(image_name):
    example_image = Image.open(image_name)
    image_height = example_image.height
    image_width = example_image.width
    image_mode = example_image.mode
    information = ('Ширина - {0}\nВысота - {1}\nЦветовая модель - {2}'.format(
            image_width, image_height, image_mode))
    return information
