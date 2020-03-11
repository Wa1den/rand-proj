#combine an ordered group of small pictures into one large

from PIL import Image

xrows = 27
ycols = 41
#27*41 = 1107

#xrows = 10
#ycols = 10

dst = Image.new('RGB', (256 * ycols, 256 * xrows))

for col in range(ycols):
	for row in range(xrows):
		img = Image.open('map/6-'+str(col)+'-'+str(row)+'.jpg')
		dst.paste(img, (256 * col, 256 * row))
dst.save('temp.jpg')
