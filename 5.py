
import urllib
import pickle

print("\n".join("".join(ch * num for (ch, num) in line) 
		for line in pickle.loads(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read())))
