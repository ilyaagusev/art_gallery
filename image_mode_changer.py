

def change_mode(image_name):
    image = image_name
    cmyk_image = image.convert('RGB')
    cmyk_image.save('rgb_{}'.format(image_name))
    print('mode changed to {}'.format(cmyk_image.mode))
