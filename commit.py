import sys, os

# compatibility between python 2 and 3
if sys.version_info >= (3,0):
	raw_input = input
	xrange = range

# list of languages/file extensions
l = []

for i in xrange(1, len(sys.argv) - 1):
	try:
		l.append(sys.argv[i + 1].lstrip('.')) # forgive using "." in file extension
	except:
		sys.stdout.write("Usage:\n")
		sys.stdout.write("'python commit.py <file extensions>'\n")
		sys.exit()

# this is admittedly a despicable number of conditionals,
# but blame python for not having a fucking switch statement

for n in xrange(0, len(l)):
	os.system("git add *.%s" % l[n])

os.system("git commit -a")
