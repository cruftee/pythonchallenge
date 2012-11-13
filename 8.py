
import urllib
import re
import bz2

html = urllib.urlopen("http://www.pythonchallenge.com/pc/def/integrity.html").read()
username, password = map(lambda x: bz2.decompress(eval("'" + x + "'")), [re.findall(x + ": '([^']+)'", html)[0] for x in ["un", "pw"]])
print "http://" + username + ':' + password + "@www.pythonchallenge.com/pc/return/good.html"
