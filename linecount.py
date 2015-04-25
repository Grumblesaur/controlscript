import sys, os
from user import userinfo

# alias long print function name to shorter name
say = sys.stdout.write

# compatibility between Python 2 and Python 3
if sys.version_info >= (3,0):
	raw_input = input

if len(sys.argv) < 2:
	say("Usage:\n")
	say("'linecount.py <source code files>'\n")
	sys.exit()

# file for comment styles
try:
	stylefile = open("%s/styles.txt" % userinfo.filepath, 'r')
except:
	say("File 'styles.txt' is missing!\n")
	sys.exit()

# code to retrieve info from style file
filetypes = []
delimiters = []
for line in stylefile:
	line = line.strip()
	if line[0:2] == "!!":
		continue
	elif line.strip() == "":
		continue
	elif line[0:2] == "@@":
		delimiters.append(line.split(" ")[1:])
	else:
		filetypes.append(line.split(" "))
	
outfile = open("linecount.txt", 'w')

# lines of code overall
overall_loc = 0
overall_com = 0
overall_wsp = 0
overall_tot = 0

# perform linecount process for every file
for f in sys.argv:

	# ignore the file being interpreted
	if f == sys.argv[0]:
		continue
	
	# ensure that the file exists
	if not os.path.isfile(f):
		say("File '%s' does not exist!\n" %f)
		continue
	
	# require a file extension to count lines of code
	try:
		# grab the file extension and use as language name
		language = f.split(".")[1]
	except:
		say("File %s has no extension!\n" %f)
		continue
	
	# open source file
	readfile = open(f, 'r')
	
	# initialize comment-delimiter strings
	comment = ""
	multistart = ""
	multiend = ""
	
	# search for the comment style
	for i in xrange(0, len(filetypes)):
		if language in filetypes[i]:
			comment = delimiters[i][0]
			multistart = delimiters[i][1]
			multiend = delimiters[i][2]
	
	# didn't find the comment style
	if comment == "":
		# provide option for user to add unknown comment styles
		say("Language %s or file extension unknown.\n" %language)
		ans = raw_input("Would you like to add it now? (Y/N): ").lower()
			
		if ans == 'y':
			# directory where we are currently
			prev = os.getcwd()
			
			# go to the script and edit it
			os.system("cd %s" %userinfo.filepath)
			os.system("%s styles.txt" %userinfo.editor)
			
			# return to the initial directory
			os.system("cd %s" %prev)
			
		# bail out and let the user restart.
		say("Linecount aborted.\n")
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
