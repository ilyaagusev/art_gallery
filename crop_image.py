

def crop_image(
    image_name,
    left_crop,
    top_crop,
    right_crop,
    bottom_crop,
):
    image = image_name
    right_crop = image.width - right_crop
    buttom_crop = image.height - bottom_crop
    coordinates = (left_crop, top_crop, right_crop, buttom_crop)
    croped = image.crop(coordinates)
    return croped
