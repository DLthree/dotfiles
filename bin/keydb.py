#!/usr/bin/python

import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("query", help="key[=val]", nargs='*', default=[])
parser.add_argument('-f', "--force", action="store_true")
parser.add_argument("--clean", action="store_true")
args = parser.parse_args()

keydb_path = os.path.expanduser("~/.keydb.json")

if args.clean and os.path.exists(keydb_path):
    os.unlink(keydb_path)

if os.path.exists(keydb_path):
    with open(keydb_path, "r") as f:
        keydb = json.load(f)
else:
    keydb = dict()

query = ' '.join(args.query)
if args.query:
    if query.find("=") != -1:
        # assignment mode
        key,value = query.split("=")
        key = key.strip()
        value = value.strip()
        if key in keydb and not args.force:
            raise Exception("fatal: key %s has value %s.  use -f to force overwrite")
        keydb[key] = value
        with open(keydb_path, "w") as f:
            json.dump(keydb, f)
        print "%s=%s" % (key, value)
    else:
        # query mode
        key = query.strip()
        print keydb[key]
