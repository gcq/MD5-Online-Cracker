import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	try:
		br = br.open("http://md5-lookup.com/livesearch.php?q=%s" % string)
		result = br.readlines()
		result = result[16].strip().replace('<td width="250">', "").replace('</td>', "")
		if not result == "":
		    if thread:
		        say(["md5-lookup.com", result])
		    return ["md5-lookup.com", result]
	except:
		pass
