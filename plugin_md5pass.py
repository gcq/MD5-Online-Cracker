import mechanize

def init():
    print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
    br = mechanize.Browser()
    br.open("http://md5pass.info/")
    br.select_form(nr=1)
    br["hash"] = string
    response = br.submit()
    for i in response.readlines():
        if "Password - " in i:
            result = i.strip().replace("Password - <b>", "").replace("</b>", "")
            result = ["hashchecker.com", result]
            if thread:
                say(result)
            return result
