import sys, os
from user import userinfo

""" This lines-of-code counting script expects a file whose comments are
	formatted such that:

		* All multi-line comments begin with the multi-line comment starting
		  delimiter at the beginning of the line.
		* All multi-line comments end with the multi-line comment ending
		  delimiter on its own line with nothing else.

	Inline comments are not counted.

	#!-delimited interpreter instructions are treated as comments in
	languages whose comment delimiter is the '#' character.
	
	Whitespace lines within multi-line comments are counted as whitespace.
	
	The end-of-file line is counted as whitespace.
	
	For best results, don't use multi-line comments and just type them out
	in individual lines with single-line comment delimiters at the start
	of each line.
"""

# compatibility between Python 2 and Python 3
if sys.version_info >= (3,0):
	raw_input = input

try:
	f = sys.argv[1]
except:
	sys.stdout.write("Usage:\n")
	sys.stdout.write("'linecount.py <input file>'\n")
	sys.exit()

# ensure that the file exists
if not os.path.isfile(f):
	sys.stdout.write("File does not exist!\n")
	sys.exit()

# require a file extension to count lines of code
try:
	# grab the file extension and use as language name
	language = f.split(".")[1]
except:
	sys.stdout.write("File has no extension!\n")
	sys.exit()

# open source file
readfile = open(f, 'r')

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
	sys.stdout.write("Language comment style or file extension unknown.\n")
	ans = raw_input("Would you like to add it now? (Y/N): ").lower()
	
	if ans == 'y':
		# directory where we are currently
		prev = os.getcwd()
		
		# go to the script and edit it
		os.system("cd %s" %userinfo.filepath)
		os.system("%s linecount.py" %userinfo.editor)
		
		# return to the initial directory
		os.system("cd %s" %prev)
		
		ans2 = raw_input("Attempt linecount again? (Y/N): ")
		if ans2.lower() == "y":
			# attempt commit again
			t = sys.argv[1]
			os.system("python %s/linecount.py %s" %(userinfo.filepath, t))
			sys.exit() # prevents infinitely recursive program calls
		else:
			sys.stdout.write("Linecount aborted.\n")
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
	# temporary variables for checking the lines in the file
	# instead of doing these operations in each of the relevant
	# conditional statements.
	temp = line.split(comment)
	temp2 = line.lstrip()[0:len(multistart)]

	# empty line logic
	if line == "":
		whitespaceLines += 1
	elif line.strip() == "":
		whitespaceLines += 1

	# comment logic
	elif (temp[0].strip() == "") and (temp[1] != ""):
		commentLines += 1

	# expect multi-line comments to begin with delimiter at start of line
	elif (isMulti == False) and (temp2 == multistart):
		isMulti = True
		commentLines += 1

	# expect multi-line comments to end only with delimiter
	elif (isMulti == True) and (line.strip() == multiend):
		commentLines += 1
		isMulti = False
	
	# any lines during a multiline comment are automatically comments
	elif isMulti:
		commentLines += 1

	# code line logic
	else:
		codeLines += 1
	
# find total length of file
total = codeLines + commentLines + whitespaceLines

# print information to console
sys.stdout.write("%s lines in file '%s'.\n" %(total, f))
sys.stdout.write("%s lines of code.\n" %codeLines)
sys.stdout.write("%s lines of comments.\n" %commentLines)
sys.stdout.write("%s lines of whitespace.\n" %whitespaceLines)
