import subprocess

try:
	res = subprocess.check_output(["zbarimg", "misc3.png"])
	print("0 barcode" in res)
except subprocess.CalledProcessError:
	print("123")
