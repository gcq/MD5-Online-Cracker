# -*- coding: utf-8 -*-

import mechanize

def init():
    print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):
    br = mechanize.Browser()
    try:
        br = br.open("http://md5-db.de/%s.html" % string)
        for i in br.readlines():
            if string in i and "verwenden" in i:
                result = i.strip().replace('<strong>Es wurden 1 m\xf6gliche Begriffe gefunden, die den Hash %s verwenden:</strong><ul><li>' % string, "").replace('</li>', "")
        if thread:
            say(["md5-db.de", result])
        return ["md5-db.de", result]
    except:
        pass
