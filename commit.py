import sys, os

# edit in the filepath to this directory and text editor name here
filepath = "/home/james/Programming/python/shellscripts"
editor = "vim"

if sys.version_info >= (3,0):
	raw_input = input

l = raw_input("Language for this git repo? ").lower()

# this is admittedly a despicable number of conditionals,
# but blame python for not having a fucking switch statement

if l == "python" or l == "py":
	os.system("git add *.py && git commit -a")

elif l == "c++" or l == "cpp":
	os.system("git add *.cpp *.h && git commit -a")

elif l == "lua":
	os.system("git add *.lua && git commit -a")

elif l == "perl" or l == "pl":
	os.system("git add *.pl && git commit -a")

elif l == "hack" or l == "assembly" or l == "asm":
	os.system("git add *.hack *.asm && git commit -a")

elif l == "hdl":
	os.system("git add *.hdl && git commit -a")

else:
	sys.stdout.write("Language not specified in commit.py.\n")
	i = raw_input("Would you like to add this language now? (Y/N): ")
	if i.lower() == "y":
		os.system("cd %s" %filepath)
		os.system("%s commit.py" %editor)
