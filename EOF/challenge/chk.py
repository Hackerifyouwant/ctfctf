import json, codecs
import requests as req

r = req.get("http://10.140.0.8/scoreboard")
txt = str(r.text)
txt = txt.split(",")
dct = {}
for i in txt:
	i = i.split("\"")
	dct[int(i[1])]=[]
	dct[int(i[1])].append(i[5])
	if len(i)>=12:
		dct[int(i[1])].append(i[12])
for i in range(1, 5):
	print("rank \#" + str(i))
	for j in dct[i]:
		print("    "+j)
