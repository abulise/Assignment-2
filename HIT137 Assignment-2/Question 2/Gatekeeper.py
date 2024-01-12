import time
from PIL import Image

current_time =int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10
print(generated_number)

image = Image.open('X:\\Python\\chapter1.jpg')

pixels = image.load()
for i in range(image.width):
    for j in range(image.height):
        r, g, b = pixels[i, j]
        r += generated_number
        g += generated_number
        b += generated_number
        pixels[i, j] = (r, g, b)


image.save('chapter1out.png')


new_image = Image.open('chapter1out.png')
red_sum = sum(pixel[0] for pixel in new_image.getdata())


print(f"The sum of the red pixel values in the new image is: {red_sum}")