from PIL import Image

from blend_image import blend_image
from crop_image import crop_image
from image_info import image_information
from merge_image_by_color import merge_rgb_image
from split_image_by_color import split_image


def crop_and_blend(color_mode, left_crop, right_crop):
    crop_1 = crop_image(color_mode, left_crop, 0, right_crop, 0)
    crop_2 = crop_image(color_mode, 50, 0, 50, 0)
    blend_crops = blend_image(crop_1, crop_2, 0.5)
    return blend_crops


image_name = Image.open('monro.jpg')
splited_image_1 = split_image(image_name)

red_color_mode = splited_image_1[0]
green_color_mode = splited_image_1[1]
blue_color_mode = splited_image_1[2]

red_image_blend = crop_and_blend(red_color_mode, 100, 0)
blue_image_blend = crop_and_blend(blue_color_mode, 0, 100)
green_color_crop = crop_image(green_color_mode, 50, 0, 50, 0)

splited_image_2 = (red_image_blend, green_color_crop, blue_image_blend)
merged_image = merge_rgb_image(splited_image_2)
merged_image.thumbnail((80, 80))
merged_image.save('monro_2.jpg')


print(image_information('monro.jpg'))
print(image_information('monro_2.jpg'))
