from PIL import Image

example_image = Image.open('example.jpg')
rotated_image = example_image.rotate(45)
rotated_image.save('rotated.jpg')
