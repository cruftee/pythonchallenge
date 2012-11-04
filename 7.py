
import urllib
import Image
import code
import os
import re

imagefile = "oxygen.png"

if not os.path.isfile(imagefile):
	with open(imagefile, "wb") as imgf:
		imgf.write(urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png").read())

imgf = Image.open(imagefile, "r")
msg = "".join([chr(y[0]) for y in [imgf.getpixel((x,48)) for x in range(0,629)] if y[0] == y[1] == y[2]])

premsg = msg[0]
sufmsg = ""
for ch in msg[1:]:
	if ch == "[" or sufmsg:
		sufmsg += ch
	elif premsg[-1] != ch:
		premsg += ch

#print premsg

next = eval("".join([x[0] for x in re.findall(".{7}", sufmsg)]))
print "".join(map(chr, next)) + ".html"
