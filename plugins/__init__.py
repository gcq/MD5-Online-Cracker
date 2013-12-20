import os, re


_regex = re.compile(r"[^_].+\.py")

PLUGINS = [i for i in os.listdir(os.path.dirname(__file__)) if _regex.match(i)]
