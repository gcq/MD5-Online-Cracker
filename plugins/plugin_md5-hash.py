import mechanize

def init():
	print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
	br = mechanize.Browser()
	br = br.open("http://www.md5-hash.com/md5-hashing-decrypt/%s" % string)
	for i in br.readlines():
		if i.find("Decrypted text for MD5 hash") != -1:
		    result = i.replace('<p class="fs-12">Decrypted text for MD5 hash <strong>' + string + '</strong> is <strong class="result">', "").replace("</strong></p>", "").strip()
		    if thread:
		        ["md5-hash.com", result]
			return ["md5-hash.com", result]
