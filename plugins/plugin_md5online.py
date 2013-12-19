import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	br.open("http://md5online.net/")
	br.select_form(nr=0)
	br["pass"] = string
	response = br.submit()
	result = ["md5online.net", response.readlines()[48].replace('<center><p>md5 :<b>' + string + '</b> <br>pass : <b>', "").replace("</b></p></table>", "").strip()]
	if not "not found in our database" in result[1]:
	    if thread:
	        say(result)
		return result
