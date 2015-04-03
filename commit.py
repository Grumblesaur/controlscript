# script to commit to a git repo for a given language

import sys, os

if sys.version_info >= (3,0):
	raw_input = input

language = raw_input("Language for this git repo? ").lower()

# this is admittedly a despicable number of conditionals,
# but blame python for not having a fucking switch statement

if language == "python" or "py":
	os.system("git add *.py && git commit -a")

elif language == "c++":
	os.system("git add *.cpp *.h && git commit -a")

elif language == "lua":
	os.system("git add *.lua && git commit -a")

elif language == "perl" or "pl":
	os.system("git add *.pl && git commit -a")

elif language == "hack" or "assembly" or "asm":
	os.system("git add *.hack *.asm && git commit -a")

elif language == "hdl":
	os.system("git add *.hdl && git commit -a")

else:
	sys.stdout.write("Language not specified in commit.py.\n")
	i = raw_input("Would you like to add this language now? (Y/N): ")
	if i.lower() == "y":
		os.system("goshell && vim commit.py")
