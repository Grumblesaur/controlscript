import sys, os
from user import userinfo

# compatibility between Python 2 and Python 3
if sys.version_info >= (3,0):
	raw_input = input

# check for file argument
if len(sys.argv) == 1 or len(sys.argv) > 2:
	# print usage instructions and bail out if given invalid arguments
	sys.stdout.write("Usage:\n")
	sys.stdout.write("'linecount.py <input file>'\n")
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

# c-family language style
cExtensions = ["c++", "cpp", "c", "cc", "h", "hpp", "cxx",
			   "hxx", "hh", "java", "cs", "m"] # fuck you objective-c
if language in cExtensions:
	comment = "//"
	multistart = "/*"
	multiend = "*/"

# lua style
elif language == "lua":
	comment = "--"
	multistart = "--[["
	multiend = "]]"

# python style
elif language == "py":
	comment = "#"
	multistart = '"""'
	multiend = '"""'

# bash shell style
elif language == "sh":
	comment = "#"
	multistart = ": '"
	multiend = "'"

# r style
elif language == "r":
	comment = "#"

# perl style
elif language == "pl":
	comment = "#"

else:
	# provide option for user to add unknown comment styles
	sys.stdout.write("Language comment style unknown.\n")
	ans = raw_input("Would you like to add it now? (Y/N) ").lower()
	
	# go there, open the file in vim	
	if ans == 'y':
		os.system("cd %s" %userinfo.filepath)
		os.system("%s linecount.py" %userinfo.editor)
		sys.exit()
	else:
		sys.exit()

# counting variables
total = 0
code = 0
noncode = 0
isMulti = False

for line in readfile:
	# empty or single-comment logic
	if line == "":
		noncode += 1
	elif line.strip() == "":
		noncode += 1
	elif line.lstrip()[0:len(comment) - 1] == comment:
		noncode += 1
	# multi-line comment logic
	elif (multistart in line) and (isMulti == False):
		noncode += 1
		isMulti = True
	elif (multiend in line) and (isMulti == True):
		noncode += 1
		isMulti = False
	elif isMulti == True:
		noncode += 1
	# actual code logic
	else:
		code += 1
# find total length of file
total = code + noncode

# print information to console
sys.stdout.write(str(total) + " lines in file '%s'.\n" %filename)
sys.stdout.write(str(code) + " lines of code.\n")
sys.stdout.write(str(noncode) + " lines of non-code.\n")
