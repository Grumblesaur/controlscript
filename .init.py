import sys, os

if sys.version_info >= (3,0):
	raw_input = input

filepath = os.getcwd()

editor = raw_input("Enter command for your preferred text editor: ")

information = '''
class userinfo(object):
	filepath = "%s"
	editor = "%s"
''' %(filepath, editor)

userfile = open("user.py", 'w')

userfile.write(information)

sys.stdout.write("Directory initialized.\n")
