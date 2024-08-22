from rembg import remove
from PIL import Image

input_path = '2.png'
output_path = 'chistoe_2.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)