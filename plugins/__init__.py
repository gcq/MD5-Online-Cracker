import os, re

_regex = re.compile(r"[^_].+\.py")

PLUGINS = [i for i in os.listdir(".") if _regex.match(i)]
