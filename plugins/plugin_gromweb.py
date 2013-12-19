import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	try:
		br = br.open("http://md5.gromweb.com/query/%s" % string)
		result = br.read()
		if thread:
		    say(["md5.gromweb.com", result])
		return ["md5.gromweb.com", result]
	except:
		pass
