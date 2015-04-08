import sys, os

# compatibility between Python 2 and Python 3
if sys.version_info >= (3,0):
	raw_input = input

# check for file argument
if len(sys.argv) == 1 or len(sys.argv) > 2:
	# print usage instructions and bail out if given invalid arguments
	sys.stdout.write("Usage:\n")
	sys.stdout.write("'linecount <input file>'\n")
	sys.exit()

filename = sys.argv[1]

if "." not in filename:
	sys.stdout.write("No file extension!\n")
	sys.exit()

language = filename.split(".")[1]

# open source file
readfile = open(filename, 'r')

comment = ""
multistart = '`````' # dummy markers for languages w/o multiline comments
multiend = '`````'

# language style options

if language == "c++" or "cpp" or "c" or "cxx" or "h" or "java":
	comment = "//"
	multistart = "/*"
	multiend = "*/"

elif language == "lua":
	comment = "--"
	multistart = "--[["
	multiend = "]]"

elif language == "py":
	comment = "#"
	multistart = '"""'
	multiend = '"""'

elif language == "sh" or "bash":
	comment = "#"
	multistart = ": '"
	multiend = "'"

elif language == "r":
	comment = "#"

else:
	# provide option for user to add unknown comment styles
	sys.stdout.write("Language comment style unknown.\n")
	ans = raw_input("Would you like to add it now? (Y/N) ").lower()
	
	# go there, open the file in vim	
	if ans == 'y':
		os.system("cd /home/james/Programming/python/linecounter")
		os.system("vim linecount.py")
		sys.exit()

# counting variables
total = 0
code = 0
noncode = 0
isMulti = False

for line in readfile:
	# begin logic for nonempty lines
	if line != "":
		# begin logic for non-whitespace lines
		if line.lstrip() != "":
			# treat comment lines as noncode
			temp = line.lstrip()
			if temp[0:len(comment)-1] == comment:
				noncode += 1
			elif temp[0:len(multistart)-1] == multistart:
				noncode += 1
				isMulti = True
			elif (multiend in line) and (isMulti == True):
				noncode += 1
				isMulti = False
			elif (multiend not in line) and (isMulti == True):
				noncode += 1
			# treat all other lines as code
			else:
				code += 1
		# treat whitespace lines as noncode
		else:
			noncode += 1
	# treat empty lines as noncode
	else:
		noncode += 1
		
# find total length of file
total = code + noncode

# print information to console
sys.stdout.write(str(total) + " lines in file '%s'.\n" %filename)
sys.stdout.write(str(code) + " lines of code.\n")
sys.stdout.write(str(noncode) + " lines of non-code.\n")
