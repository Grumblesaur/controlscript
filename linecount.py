import sys, os

if sys.version_info >= (3,0):
	raw_input = input

if len(sys.argv) == 1:
	sys.stdout.write("Usage:\n")
	sys.stdout.write("'python linecount.py <input file>'\n")
	sys.exit()
else:
	filename = sys.argv[1]
	language = filename.split(".")[1]

readfile = open(filename, 'r')

comment = ""
multistart = '`````'
multiend = '`````'

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
	sys.stdout.write("Language comment style unknown.\n")
	ans = raw_input("Would you like to add it now? (Y/N) ").lower()
	
	if ans == 'y':
		os.system("cd /home/james/Programming/python/linecounter")
		os.system("vim linecount.py")
		sys.exit()

# counting variables
total = 0
code = 0
noncode = 0
multiline = False

for line in readfile:
	# count indented comments as noncode
	if (line.lstrip()[0:len(comment)-1] == comment) or (multiline == True):
		noncode += 1
	# count multiline comment start as noncode
	elif multistart in line:
		noncode += 1
		multiline = True
	# count multiline comment end as noncode
	elif (multiline == True) and (multiend in line):
		noncode += 1
		multiline = False
	# count empty lines as noncode
	elif line.strip() == "":
		noncode += 1
	# count logical lines as code
	else:
		code += 1

# find total length of file
total = code + noncode

# print information to console
sys.stdout.write(str(total) + " lines in file '%s'.\n" %filename)
sys.stdout.write(str(code) + " lines of code.\n")
sys.stdout.write(str(noncode) + " lines of non-code.\n")
