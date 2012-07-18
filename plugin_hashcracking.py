import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	try:
		br = br.open("http://md5.hashcracking.com/search.php?md5=%s" % string)
		result = br.read().strip()
		result = result.replace("Cleartext of %s is " % string, "")
		if not result == "No results returned.":
		    if thread:
		        say(["md5.hashcracking.com", result])
		    return ["md5.hashcracking.com", result]
	except:
		pass
