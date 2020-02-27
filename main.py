from PIL import Image

"""
	# rename files

import os

for x in range(2, 62):
	if (x < 10):
		os.rename('C001H001S000600000' + str(x) + '.tif', 'image' + str(x) + '.tif')
	else:
		os.rename('C001H001S00060000' + str(x) + '.tif', 'image' + str(x) + '.tif')
"""

for num_images in range(1, 2):
	image = Image.open('image' + str(num_images) + '.tif') # read file
	width, height = image.size # get sizes
	rgb_image = image.convert('RGB') # convert image to rgb palette
	# print(width, height)

"""
	for x in range(1, width):
		for y in range(x, height):
			#if ( ((x % 4) == 0) && ((y % 4) == 0) ): 
			#	r, g, b = rgb_image.getpixel((x, y)) # read each pixel horizontally
"""

field_start = 1
field_end = 1
occurencies = 0;

for x in range(1, width):
	r, g, b = rgb_image.getpixel((x, 1))
	w, h, y = rgb_image.getpixel((x, height - 1))

	if ( r > 150):
		if ( abs(w - r) < 15 ):
			#print("our field");
			#print(x)
			if (occurencies == 0):
				field_start = x
			field_end = x
			occurencies += 1;

print("our field is from " + str(field_start) + " to " + str(field_end))

for x in range(field_start, field_end):
	for y in range(x, height):