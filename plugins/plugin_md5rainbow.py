import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	br = br.open("http://www.md5rainbow.com/%s" % string)
	result = br.readlines()[29].replace('<br/><p style="font-size: 9pt; line-height: 48px;"><a style="text-decoration: none;" href=%s><img src="http://about.md5rainbow.com/img/star.png" width=48 height=48 alt=Bookmark style="vertical-align: middle;"/> http://www.MD5rainbow.com/%s</a></p>' % (string, string), "").strip()
	result = ["md5online.net", result]
	if not "Sorry, no reverse string was found" in result[1]:
	    if thread:
	        say(result)
		return result
