import mechanize
from xgoogle.search import GoogleSearch

def init():
    print "[%s] enabled" % __name__.upper()

def say(string):
    print "[%s] %s" % (__name__.upper(), string)

def run(string, thread=False):

#---------------Parsers definition---------------------

    class template():

        def __init__(self):
            pass #Nothing needed in __init__()

        def run(self, string):

            query = "site:ReverseIndexSite %s" % string

            if not thread:
                say("Querying Google: '%s'" % query)

            gs = GoogleSearch(query)
            gs.results_per_page = 10
            results = gs.get_results()
            if len(results) >= 1:
                result = None #At the end result must be a string containing the decoded md5 hash
                result = ["ReverseIndexSite", result]
                if thread:
                    say(result)
                return result


    class md5database():

        def __init__(self):
            pass

        def run(self, string):

            query = "site:http://md5-database.org/md5 %s" % string

            if not thread:
                say("Querying Google: '%s'" % query)

            gs = GoogleSearch(query)
            gs.results_per_page = 10
            results = gs.get_results()
            if len(results) >= 1:
                result = str(results[0].title)[results[0].title.find(" - ") + 3:results[0].title.find(" {")]
                result = ["md5-database.org", result]
                if thread:
                    say(result)
                return result


    class md5pass():

        def __init__(self):
            pass

        def run(self, string):

            query = "site:http://md5pass.com %s" % string

            if not thread:
                say("Querying Google: '%s'" % query)

            gs = GoogleSearch(query)
            gs.results_per_page = 10
            results = gs.get_results()
            if len(results) >= 1:
                for result in results:
                    print result.title
                    print result.desc
                result = None
                result = ["md5pass.com", result]
                if thread:
                    say(result)
                return result


    class md5hashcracker():

        def __init__(self):
            pass

        def run(self, string):

            query = "site:md5hashcracker.appspot.com/hashdb %s" % string

            if not thread:
                say("Querying Google: '%s'" % query)

            gs = GoogleSearch(query)
            gs.results_per_page = 10
            results = gs.get_results()
            if len(results) >= 1:
                for result in results:
                    print result.title
                    print result.desc
                result = None
                result = ["md5hashcracker.appspot.com", result]
                if thread:
                    say(result)
                return result


#--------------------------------------------------------------------------


    sites = [
            md5database,
            md5pass,
            md5hashcracker
            ]

    result = ["google.com", []]

    for site in sites:
        result[1].append(site().run(string))

    for res in result[1]:
        if res != None:
            return result
