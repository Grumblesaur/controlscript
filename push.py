import os, sys

if sys.version_info >= (3,0):
	raw_input = input

destination = raw_input("Target '(u)pstream' or '(o)rigin'? ").lower()
branch = raw_input("Enter branch (leave blank for 'master') ").lower()

if destination == "":
	sys.stdout.write("No destination selected!\n")
	sys.exit()

if branch == "" or "m":
	branch = "master"

if destination == "upstream" or destination == "u":
	os.system("git push upstream %s" %branch)

elif destination == "origin" or destination == "o":
	os.system("git push origin %s" %branch)

else:
	sys.stdout.write("Destination not found!\n")
