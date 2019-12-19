from PIL import Image


def image_info(image_name):
    example_image = Image.open(image_name)
    image_height = example_image.height
    image_width = example_image.width
    image_mode = example_image.mode
    print(
        'Ширина - {0}\nВысота - {1}\nЦветовая модель - {2}'.format(
            image_height, image_width, image_mode
        ))
