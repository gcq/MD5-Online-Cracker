import argparse
import time
import concurrent.futures as futures
from importlib import machinery

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

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--hash",
                    nargs="+",
                    help="Hash or hashes to look up")
parser.add_argument("-t", "--threads",
                    type=int,
                    default=1,
                    help="Set the size of the threadpool")

args = parser.parse_args()
print(args)


#---------------------MAIN----------------------------

print(machinery.SourceFileLoader("plugin_goog", ".").load_module())

"""
def testfunc(i):
    time.sleep(1)
    return "I'm {}".format(i)

with futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
    future_list = {executor.submit(testfunc, i):i for i in range(10)}
    for future in futures.as_completed(future_list):
        print(future_list[future], future.result())
"""


"""
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
"""
