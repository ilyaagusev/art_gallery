from PIL import Image


def merge_rgb_image(rgb_tuple):
    red = rgb_tuple[0]
    green = rgb_tuple[1]
    blue = rgb_tuple[2]
    merged_image = Image.merge('RGB', (red, green, blue))
    return merged_image
