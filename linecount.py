import sys, os
from user import userinfo

# compatibility between Python 2 and Python 3
if sys.version_info >= (3,0):
	raw_input = input

if len(sys.argv) < 2:
	sys.stdout.write("Usage:\n")
	sys.stdout.write("'linecount.py <source code files>'\n")
	sys.exit()

outfile = open("linecount.txt", 'w')

# lines of code overall
overall_loc = 0
overall_com = 0
overall_wsp = 0
overall_tot = 0

for f in sys.argv:

	# ignore the file being interpreted
	if f == sys.argv[0]:
		continue
	
	# ensure that the file exists
	if not os.path.isfile(f):
		sys.stdout.write("File '%s' does not exist!\n" %f)
		continue
	
	# require a file extension to count lines of code
	try:
		# grab the file extension and use as language name
		language = f.split(".")[1]
	except:
		sys.stdout.write("File %s has no extension!\n" %f)
		continue
	
		# open source file
	readfile = open(f, 'r')
	
	comment = "" # guaranteed not to be empty during counting process
	multistart = '`````' # dummy marks for languages w/o multiline comments
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
		sys.stdout.write("Language or file extension unknown.\n")
		ans = raw_input("Would you like to add it now? (Y/N): ").lower()
			
		if ans == 'y':
			# directory where we are currently
			prev = os.getcwd()
			
			# go to the script and edit it
			os.system("cd %s" %userinfo.filepath)
			os.system("%s linecount.py" %userinfo.editor)
			
			# return to the initial directory
			os.system("cd %s" %prev)
			
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
		
		# expect multiline comments to begin with delimiter at start of line
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
	
	# add to total for output file summary
	overall_loc += codeLines
	overall_com += commentLines
	overall_wsp += whitespaceLines
	overall_tot += total
	
	# print information to console
	outfile.write("%s lines in file '%s'.\n" %(total, f))
	outfile.write("%s lines of code.\n" %codeLines)
	outfile.write("%s lines of comments.\n" %commentLines)
	outfile.write("%s lines of whitespace.\n\n" %whitespaceLines)

# print summary information about the files passed
outfile.write("%s lines in files overall.\n" %overall_tot)
outfile.write("%s lines of code.\n" %overall_loc)
outfile.write("%s lines of comments.\n" %overall_com)
outfile.write("%s lines of whitespace.\n" %overall_wsp)
