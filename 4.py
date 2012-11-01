import urllib
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
token = "12345"
print "Walking the linked list"
dots = 0
while token:
	body = urllib.urlopen(url + token.strip()).readline()
	if token.endswith(".html"):
		print "\n" + token
		break
	token = body.split(" is ")[-1].strip()
	print ".",
	dots += 1
	if dots > 79:
		dots = 0
		print


