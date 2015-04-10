import sys, os
from user import userinfo

# compatibility between Python 2 and Python 3
if sys.version_info >= (3,0):
	raw_input = input

# check for file argument
if len(sys.argv) != 2:
	# print usage instructions and bail out if given invalid arguments
	sys.stdout.write("Usage:\n")
	sys.stdout.write("'linecount.py <input file>'\n")
	sys.exit()

filename = sys.argv[1]

# require known file extension to count lines of code
if "." not in filename:
	sys.stdout.write("No file extension!\n")
	sys.exit()

# grab the file extension and use as language name
language = filename.split(".")[1]

# open source file
readfile = open(filename, 'r')

comment = "" # guaranteed not to be empty during counting process
multistart = '`````' # dummy markers for languages w/o multiline comments
multiend = '`````'   # program would blow chunks w/ empty strings

# language style options

# c-like comment styles
cLike = ["c++", "cpp", "c", "cc", "h", "hpp", "cxx",
			   "hxx", "hh", "java", "cs", "m", "d", "b"]
# lua-like comment styles
luaLike = ["lua", "adb", "ads", "e", "ex", "exw", "edb", "hs", "lhs"]

# python-like comment styles
pythonLike = ["py", "r", "sh", "pl", "jl", "rbw", "rb"]

# lisp-like comment styles
lispLike = ["clj", "cljs", "edn", "lisp", "lsp", "l", "cl", "fasl"]

if language in cLike:
	comment = "//"
	multistart = "/*"
	multiend = "*/"

elif language in luaLike:
	comment = "--"
	if language == "lua":
		multistart = "--[["
		multiend = "]]"

elif language in pythonLike:
	comment = "#"
	if language == "py":
		multistart = '"""'
		multiend = '"""'
	elif language == "jl":
		multistart = "#="
		multiend = "=#"
	elif language == "rb" or language == "rbw":
		multistart = "=begin"
		multiend = "=end"

elif language in lispLike:
	comment = ";"

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
		sys.stdout.write("Linecount aborted.\n")
		sys.exit()

# counting variables
total = 0
codeLines = 0
commentLines = 0
whitespaceLines = 0
isMulti = False

for line in readfile:
	temp = line.split(comment)
	
	# empty line logic
	if line == "":
		whitespaceLines += 1
	elif line.strip() == "":
		whitespaceLines += 1
	# comment logic
	elif (temp[0].strip() == "") and (temp[1] != ""):
		commentLines += 1
	# multi-line comment logic
	elif (isMulti == False) and (multistart in line):
		isMulti = True
		commentLines += 1
	elif (isMulti == True) and (multiend in line):
		commentLines += 1
		isMulti = False
	elif isMulti and (multiend not in line) and (multistart not in line):
		commentLines += 1
	# code line logic
	else:
		codeLines += 1
	
# find total length of file
total = codeLines + commentLines + whitespaceLines

# print information to console
sys.stdout.write(str(total) + " lines in file '%s'.\n" %filename)
sys.stdout.write(str(codeLines) + " lines of code.\n")
sys.stdout.write(str(commentLines) + " lines of comments.\n")
sys.stdout.write(str(whitespaceLines) + " lines of whitespace.\n")
