import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	br.open("http://www.stringfunction.com/md5-decrypter.html?s=%s" % string)
	br.select_form("form_md5_decrypter")
	if br["result"]:
	    result = br["result"]
	    if thread:
	        say(["stringfunction.com", result])
		return ["stringfunction.com", result]
