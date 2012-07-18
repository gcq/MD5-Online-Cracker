import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	try:
		br = br.open("http://goog.li/?t=%s" % string)
		result = br.readlines()[5].strip()
		result = result[result.find("=") + 1:]
		if not result == "# hash not found on goog.li :(":
		    if thread:
		        say(["goog.li", result])
		    return ["goog.li", result]
	except:
		pass
