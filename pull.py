import os, sys

if sys.version_info >= (3,0):
	raw_input = input

target = raw_input("Target '(u)pstream' or '(o)rigin'? ").lower()

branch = raw_input("Branch (leave blank for 'master'): ").lower()

if branch == "" or "m":
	branch = "master"

if target == "upstream" or target == "u":
	os.system("git pull upstream %s" %branch)

elif target == "origin" or target == "o":
	os.system("git pull origin %s" %branch)

else:
	sys.stdout.write("Target repo not specified in script file.\n")
