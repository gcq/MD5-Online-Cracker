import os, re


_regex = re.compile(r"([^_].+)\.py")

PLUGINS = []
for i in os.listdir(os.path.dirname(__file__)):
    m = _regex.match(i)
    if m:
        PLUGINS.append(m.group(1))
