import os, glob, optparser, threadpuul

#--------------Function definition--------------------

def cleanup():
	filelist = glob.glob("*.py?")
	for f in filelist:
		os.remove(f)
        
def load_plugin(name):
    mod = __import__("plugin_%s" % name)
    return mod

def load_plugins(config_file):
    plugins = []
    pnames = []
    with open(config_file, "r") as fh:
        for line in fh:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            pnames.append(line)
        pnames.sort()
        for i in pnames:
            plugins.append(load_plugin(i))
    return plugins

#-----------------Option parsing----------------------

p = optparser.parser()
options = p.run()
if "hash" in options:
    crack = options["hash"]
else:
    print "Hash needed!"
    exit()
if "threads" in options:
    if options["threads"] != True:
        threadcount = options["threads"]
else:
    threadcount = 2

if "help" in options:
    print """
    Use help=[hash] to set the has to be cracked
    Use threads=[integer] to start the threaded process
    """

#---------------------MAIN----------------------------

cleanup()

#Load all plugins in the list
plugins = load_plugins("plugins.list")

print "\nInitilizing plugins...\n"

for i in plugins:
    i.init()

if threadcount != 0:
    print "\n\nCracking started (using threads)\n"
    pool = threadpuul.ThreadPool(threadcount)
    for i in plugins:
        pool.add_task(i.run, crack, True)
    pool.wait_completion()
    print
else:
    print "\n\nCracking started\n"
    result = None
    for i in plugins:
        result = i.run(crack)
        if result != None:
            print "Web: %s" % result[0]
            print "Result: %s" % result[1]
            break
    if not result:
        print "\nNo match found\n"
    
cleanup()
