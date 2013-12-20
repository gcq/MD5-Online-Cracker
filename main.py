import argparse
import logging
import concurrent.futures as futures
import importlib
import plugins
import sys

h = "9cdfb439c7876e703e307864c9167a15"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
stream = logging.StreamHandler(sys.stdout)
stream.setFormatter(logging.Formatter("[{levelname}] -> {message}", style="{"))
logger.addHandler(stream)

requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)


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


def worker(pname, h):
    try:
        p = importlib.import_module("plugins.{}".format(pname))
    except:
        logger.warning("{} has errors! Contact developer".format(pname))
        return None
    try:
        return p.get_plaintext(h)
    except:
        logger.warning("{} lacks the needed API".format(pname))
        return None

with futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
    future_list = {executor.submit(worker, i, h):i for i in plugins.PLUGINS}
    for future in futures.as_completed(future_list):
        result = future.result()
        if result:
            logger.info((future_list[future], result))
