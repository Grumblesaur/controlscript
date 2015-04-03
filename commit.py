# script to commit to a git repo for a given language

import sys, os

if sys.version_info >= (3,0):
	raw_input = input

language = raw_input("Language for this git repo? ").lower()

if language == "python" or language == "py":
	os.system("git add *.py && git commit -a")
elif language == "c++":
	os.system("git add *.cpp *.h && git commit -a")
elif language == "lua":
	os.system("git add *.lua && git commit -a")
elif language == "perl":
	os.system("git add *.pl && git commit -a")
else:
	sys.stdout.write("Language not specified in commit.py.\n")
