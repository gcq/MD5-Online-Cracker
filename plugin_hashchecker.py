import mechanize

def init():
    print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
    br = mechanize.Browser()
    br.open("http://www.hashchecker.com/index.php?_sls=search_hash")
    br.select_form("form1")
    br["search_field"] = string
    response = br.submit()
    for i in response.readlines():
        if "Your md5 hash is :" in i:
            result = i.strip().replace('<td><li>Your md5 hash is :<br><li>%s is <b>' % string, "").replace('</b> used charlist :2</td>', "")
            result = ["hashchecker.com", result]
            if thread:
                say(result)
            return result
