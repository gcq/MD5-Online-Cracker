import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	br.open("http://md5.rednoize.com/")
	br.select_form("searchform")
	br["q"] = string
	response = br.submit()
	result = ["md5.rednoize.com", response.readlines()[71].replace('<div id="result" >', "").replace("</div>", "").strip()]
	if not result[1] == '<div id="result" style="display:none;">':
	    if thread:
	        say(result)
		return result
