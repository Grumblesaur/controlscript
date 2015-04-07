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
multistart = ''
multiend = ''

if language == "c++" or "cpp" or "c" or "cxx":
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

else:
	sys.stdout.write("Language comment style unknown.\n")
	ans = raw_input("Would you like to add it now? (Y/N) ").lower()
	
	if ans == 'y':
		os.system("cd /home/james/Programming/python/linecounter")
		os.system("vim linecount.py")

# counting variables
total = 0
code = 0
noncode = 0
multiline = False

for line in readfile:
	if (line[0:1] == comment) or (multiline == True):
		noncode += 1
	elif line[0:len(multistart)-1] == multistart:
		noncode += 1
		multiline = True
	elif (multiline == True) and (multiend in line):
		noncode += 1
		multiline = False
	elif line.strip() == "":
		noncode += 1
	else:
		code += 1

total = code + noncode

sys.stdout.write(str(total) + " lines in file '%s'.\n" %filename)
sys.stdout.write(str(code) + " lines of code.\n")
sys.stdout.write(str(noncode) + " lines of non-code.\n")
