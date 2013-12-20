import argparse
import logging
import concurrent.futures as futures
import importlib
import plugins
import sys


logger = logging.getLogger()
logger.setLevel(logging.INFO)
stream = logging.StreamHandler(sys.stdout)
stream.setFormatter(logging.Formatter("[{levelname}] -> {message}", style="{"))
logger.addHandler(stream)


parser = argparse.ArgumentParser()
parser.add_argument("-H", "--hash",
                    nargs="+",
                    help="Hash or hashes to look up")
parser.add_argument("-t", "--threads",
                    type=int,
                    default=1,
                    help="Set the size of the threadpool")
parser.add_argument("-q", "--quiet",
                    action="store_true",
                    help="Just outputs hash:plaintext pairs")

args = parser.parse_args()


def worker(pname):
    p = importlib.import_module("plugins.{}".format(pname))
    return p

with futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
    future_list = {executor.submit(worker, i):i for i in plugins.PLUGINS}
    for future in futures.as_completed(future_list):
        print(future_list[future], future.result())
