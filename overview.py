from PIL import Image


def rotate_image(image_name):
    example_image = Image.open(image_name)
    rotated_image = example_image.rotate(45)
    rotated_image.save('rotated_{0}'.format(image_name))
