from PIL import Image

W, H = 384, 625

# W, H
qr = Image.open("misc1.png")
pix = qr.load()
"""
cnt = 0
for i in range(H):
	for j in range(W):
		cnt += pix[i, j] == 0
print(cnt)
"""
"""
f = open("1.csv", "w")
for i in range(H):
	tmp = ""
	ti = i
	#ti = i % W
	for j in range(0, W):
		tmp += str(int(pix[j, ti] == 0)) + ','
	
	for j in range(0, ti):
		tmp += str(int(pix[j, ti] == 0)) + ','
	
	print(tmp[:-1])
	f.write(tmp[:-1] + "\n")
print("\n\n")
f.close()
"""
f = open("tmp.txt", "w")
for i in range(H):
	for j in range(W):
		if pix[j, i] != 0:
			f.write("#")
		else:
			f.write(".")
		#f.write(str(int(pix[j, i] != 0)))
f.close()

