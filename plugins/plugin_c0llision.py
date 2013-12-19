import mechanize

def init():
    print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
    br = mechanize.Browser()
    br.open("http://c0llision.net/webcrack")
    br.select_form(nr=0)
    br["hash[_input_]"] = string
    response = br.submit()
    result = ["c0llision.net", response.readlines()[32].replace('<td class="plaintext">', "").replace("</td>", "").strip()]
    if not result[1] == '<td class="plaintext" />':
        if thread:
            say(result)
        return result
