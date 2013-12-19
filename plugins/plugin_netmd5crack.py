import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	br.open("http://netmd5crack.com/cracker/")
	br.select_form(nr=0)
	br["InputHash"] = string
	response = br.submit()
	result = ["netmd5crack.com", response.readlines()[19].replace('<tr><td class="border">' + string + '</td><td class="border">', "").replace("</td></tr></table>\n", "")]
	if not result[1] == "Sorry, we don't have that hash in our database.":
	    if thread:
	        say(result)
		return result
