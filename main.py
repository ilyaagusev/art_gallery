from PIL import Image

from blend_image import blend_image
from crop_image import crop_image
from merge_image_by_color import merge_rgb_image
from split_image_by_color import split_image


def crop_and_blend(color_mode, left_crop, right_crop):
    crop_1 = crop_image(color_mode, left_crop, 0, right_crop, 0)
    crop_2 = crop_image(color_mode, 50, 0, 50, 0)
    blend_crops = blend_image(crop_1, crop_2, 0.5)
    return blend_crops


image_name = Image.open('monro.jpg')
red_channel, green_channel, blue_channel = split_image(image_name)

red_image_blend = crop_and_blend(red_channel, 100, 0)
blue_image_blend = crop_and_blend(green_channel, 0, 100)
green_color_crop = crop_image(blue_channel, 50, 0, 50, 0)

splited_image_2 = (red_image_blend, green_color_crop, blue_image_blend)
merged_image = merge_rgb_image(splited_image_2)
merged_image.thumbnail((80, 80))
merged_image.save('monro_2.jpg')
