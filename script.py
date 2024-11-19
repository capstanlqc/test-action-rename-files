#!/usr/bin/python

import sys
import os
from pathlib import Path

filepath = sys.argv[1]
filestem = Path(filepath).stem
parentdir = Path(filepath).parent

config_fpath = os.path.join(parentdir, "config.txt")

if not os.path.isfile(filepath) and not os.path.isfile(filepath + ".off"):
    print("file not found, nothing else to do")
    sys.exit()

if not os.path.isfile(config_fpath):
    print("config not found, nothing else to do")
    sys.exit()

with open(config_fpath) as f:
    config = f.read().strip()

if config == "OFF" and os.path.isfile(os.path.join(parentdir, f"{filestem}.tmx")):
    print(f"Rename {filestem}.tmx to {filestem}.tmx.off")
    os.rename(f"{parentdir}/{filestem}.tmx", f"{parentdir}/{filestem}.tmx.off")
elif config == "ON" and os.path.isfile(os.path.join(parentdir, f"{filestem}.tmx.off")):
	print(f"Rename {filestem}.tmx.off to {filestem}.tmx")
	os.rename(f"{parentdir}/{filestem}.tmx.off", f"{parentdir}/{filestem}.tmx")