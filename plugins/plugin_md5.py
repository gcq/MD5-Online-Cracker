import mechanize

def init():
    print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
    br = mechanize.Browser()
    br.open("http://www.md5.net/cracker.php")
    br.select_form(nr=0)
    br["hash"] = string
    response = br.submit()
    result = ["md5.net", response.readlines()[39].replace('<input type="text" id="hash" size="32" value="', "").replace('"/>', "").strip()]
    if not result[1] == "Entry not found.":
        if thread:
            say(result)
        return result
