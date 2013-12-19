import mechanize

def init():
    print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):

    br = mechanize.Browser()
    if not thread:
        say("Reading: http://md5hashcracker.appspot.com/hashdb/a1") 
    br = br.open("http://md5hashcracker.appspot.com/hashdb/a1")
    if not thread:
        say("Parsing data from db") 
    for line in br.readlines():
        if string in line:
            break

    line = line.split(string)[0]
    result = line.replace("<tr>", "").replace("<td>", "").replace("</td>", "")
    result = ["md5hashcracker.appspot.com", result]
    if not "html" in result[1]:
        if thread:
            say(result)
        return result
