from image_mode_changer import change_mode
from image_info import image_info
from overview import rotate_image

example_image = 'cmyk.jpg'


def main():
    rotate_image(example_image)
    image_info(example_image)
    change_mode(example_image)


if __name__ == "__main__":
    main()
