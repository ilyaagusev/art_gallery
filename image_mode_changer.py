

def change_mode(example_image):
    image = Image.open(example_image)
    cmyk_image = image.convert('RGB')
    cmyk_image.save('rgb_{}'.format(example_image))
    print('mode changed to {}'.format(cmyk_image.mode))
