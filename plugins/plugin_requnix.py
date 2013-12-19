import mechanize

def init():
    print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
    br = mechanize.Browser()
    try:
        br = br.open("http://requnix.tk/md5/api/txt.php?md5=%s" % string)
        result = br.read().strip()
        if not result == "":
            if thread:
                say(["requnix.tk", result])
            return ["requnix.tk", result]
    except:
        pass
