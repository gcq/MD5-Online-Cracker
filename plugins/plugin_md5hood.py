import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	br.open("http://md5hood.com/index.php/cracker/crack")
	br.select_form(nr=0)
	br["md5"] = string
	response = br.submit()
	result = ["md5hood.com", response.readlines()[47].replace('<div class="result_true">', "").replace("</div>", "").strip()]
	if not "That hash could not be cracked." in result[1]:
	    if thread:
	        say(result)
		return result
