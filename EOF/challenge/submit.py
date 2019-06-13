import requests as req

flag=raw_input("Please input FLAG:")
print (flag)
r = req.get("http://10.140.0.8/submit?token=gsOqIRSW&flag=EOF{"+flag+"}")
print(r.text)
