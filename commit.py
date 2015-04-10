import sys, os
from user import userinfo

if sys.version_info >= (3,0):
	raw_input = input

if len(sys.argv) != 2:
	# when improper argument count is passed, print usage and exit
	sys.stdout.write("Usage:\n")
	sys.stdout.write("commit <language name or file extension w/o '.'\n")
	sys.exit()

l = sys.argv[1]

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
	ans = raw_input("Would you like to add this language now? (Y/N): ")
	if ans.lower() == "y":
		# directory where we are currently
		prev = os.getcwd()
		
		# go to the script and edit it
		os.system("cd %s" %userinfo.filepath)
		os.system("%s commit.py" %userinfo.editor)
		
		# return to initial directory
		os.system("cd %s" %prev)
		
		ans = raw_input("Attempt commit again? (Y/N): ")
		if ans.lower == "y":
			# attempt commit again
			os.system("python %s/commit.py %s" %(userinfo.filepath, l))
		else:
			sys.stdout.write("Commit aborted.\n")
			sys.exit()
	else:
		sys.stdout.write("Commit aborted.\n")
		sys.exit()
