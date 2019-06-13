from PIL import Image

# W, H
qr = Image.open("misc3.png")
pix = qr.load()

for i in range(27):
	tmp = ""
	for j in range(27):
		tmp += str(int(pix[j, i] == 0))
	print(tmp)

print("\n\n")
for i in range(0, 27, 2):
	tmp = ""
	for j in range(27):
		tmp += str(int(pix[j, i] == 0)) + ','
	print(tmp[:-1] + '\n')
print("\n\n")
for i in range(1, 28, 2):
	tmp = ""
	for j in range(27):
		tmp += str(int(pix[j, i] == 0)) + ','
	print(tmp[:-1] + '\n')

