from collections import defaultdict
import argparse
import concurrent.futures as futures
import importlib
import logging
import plugins
import sys


def worker(pname, h):
    try:
        p = importlib.import_module("plugins.{}".format(pname))
    except:
        logger.warning("{} has errors! Contact developer".format(pname))
        return None
    try:
        return p.get_plaintext(h)
    except AttributeError:
        logger.warning("{} lacks the needed API".format(pname))
        return None


def do_hash(h):
    with futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_list = {executor.submit(worker, i, h): i for i in plugins.PLUGINS}
        confidence = defaultdict(int)
        for future in futures.as_completed(future_list):
            result = future.result()

            if result:
                logger.debug("{plugin}: '{res}'".format(plugin=future_list[future], res=result))
                confidence[result] += 1
                level = confidence[result]
                logger.debug("Confidence level for '{res}': {level}".format(res=result, level=level))
                if level >= args.confidence:
                    logger.debug("Confident about '{}'".format(result))
                    logger.info("{hash} = '{res}'".format(hash=h, res=result))
                    for future in future_list:
                        future.cancel()
                    break
        if level < args.confidence:
            most = sorted(confidence, key=confidence.get)[0]
            logger.info("{hash} = '{res}' (low confidence)".format(hash=h, res=most))
        if len(confidence) == 0:
            logger.info("{} not found".format(h))


logger = logging.getLogger()
logger.setLevel(logging.INFO)
stream = logging.StreamHandler(sys.stdout)
stream.setFormatter(logging.Formatter("[{levelname}] -> {message}", style="{"))
logger.addHandler(stream)

requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)


parser = argparse.ArgumentParser()
hashinput = parser.add_mutually_exclusive_group(required=True)
hashinput.add_argument("-H", "--hash",
                       nargs="+",
                       help="Hash or hashes to look up")
hashinput.add_argument("-F", "--file",
                       type=argparse.FileType('r'),
                       default=sys.stdin,
                       help="File to take hashes from. One per line")
parser.add_argument("-t", "--threads",
                    type=int,
                    default=1,
                    help="Set the size of the threadpool")
parser.add_argument("-v", "--verbose",
                    action="store_true",
                    help="Set logging to debug level")
parser.add_argument("--confidence",
                    type=int,
                    default=3,
                    help="Confidence of results")

args = parser.parse_args()

if args.verbose:
    logger.setLevel(logging.DEBUG)


logger.debug("""

+--------------------+
| MD5-ONLINE-CRACKER |
+--------------------+
""")
logger.debug("{} pluigns".format(len(plugins.PLUGINS)))

logger.debug("Input hash list: {}".format(args.hash))

for h in args.hash:
    logger.debug("Working on {}".format(h))
    do_hash(h)
