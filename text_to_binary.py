from PIL import Image

text = '''Text goes here, I was too lazy to make this into a command-line utility lol, might implement in the future.'''

binaryText = ''.join(format(ord(char), '08b') for char in text)
binaryLength = int(len(binaryText))
width = (binaryLength + 1) // round(round(binaryLength / 8) * 0.1)
height = (binaryLength + 1) // width + 1

print(binaryText, binaryLength)

img = Image.new(mode="RGB", size=(width, height), color = (255, 255, 255))

count = 0
for j in range(height):
	for i in range(width):
		if (count < binaryLength):
			if(binaryText[count] == '1'):
				img.putpixel((i,j), (0, 0, 0))
			count += 1
		else:
			img.putpixel((i,j), (255, 0, 0))
			break

img.save("output.png")
img.show()
