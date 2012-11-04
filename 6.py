
import urllib
import zipfile
import os
import re
import shutil

def get_hint(hint):
	with open(os.path.join("channel", hint + ".txt")) as fobj:
		try:
			return re.findall("([0-9]{2,})", fobj.read())[0]
		except:
			return None

def main():
	with open("channel.zip", "wb") as fobj:
		fobj.write(urllib.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip").read())

	if not os.path.isdir("channel"):
		os.mkdir("channel")

	comments = {}
	with zipfile.ZipFile("channel.zip") as zipf:
		comments = dict((x.filename, x.comment) for x in zipf.infolist())
		zipf.extractall("channel")

	next = get_hint("readme")
	while next:
		next = get_hint(next)
		if next:
			print comments[next + ".txt"],


if __name__ == "__main__":
	main()
