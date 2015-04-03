import os, sys

if sys.version_info >= (3,0):
	raw_input = input

destination = raw_input("Target 'upstream' or 'origin'?").lower()
branch = raw_input("Enter branch (leave blank for 'master'")

if branch == "":
	branch = "master"

if destination == "upstream":
	os.system("git push upstream %s" %branch)

elif destination == "origin":
	os.system("git push origin %s") %branch)

else:
	sys.stdout.write("Destination not found.\n")
