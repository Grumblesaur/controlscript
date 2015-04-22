import sys, os

# compatibility between python 2 and 3
if sys.version_info >= (3,0):
	xrange = range

# list of languages/file extensions
l = []

for k in sys.argv:
	try:
		l.append(k.lstrip('.')) # forgive using "." in file extension
	except:
		sys.stdout.write("Usage:\n")
		sys.stdout.write("'python commit.py <file extensions>'\n")
		sys.exit()

if os.path.isfile("Makefile"):
	os.system("git add Makefile")
elif os.path.isfile("makefile"):
	os.system("git add makefile")

for n in l[1:]:
	os.system("git add *.%s" % n)

os.system("git commit -a")
