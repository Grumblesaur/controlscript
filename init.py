import sys, os

say = sys.stdout.write

if sys.version_info >= (3,0):
	raw_input = input

filepath = os.getcwd()

editor = raw_input("Enter command for your preferred text editor: ")

# create .py file with user's info to be called in other scripts

information = '''
class userinfo(object):
	filepath = "%s"
	editor = "%s"
''' %(filepath, editor)

# write the above information into user.py to create a working import file
userfile = open("user.py", 'w')
userfile.write(information)
userfile.close()

say("Directory initialized.\n")

# append aliases to bash alias file if requested

ans = raw_input("Would you like to use aliases for these scripts? (y/N):")

if ans.lower() != "y":
	sys.exit()

name = raw_input("Enter your username on this system: ")

# open this file in the user's home folder
aliasfile = open("/home/%s/.bash_aliases" %name, 'a')
aliases = '''
alias commit='python %s/commit.py'
alias push='python %s/push.py'
alias pull='python %s/pull.py'
alias linecount='python %s/linecount.py'
''' %(filepath, filepath, filepath, filepath)

aliasfile.write(aliases)
say("Aliases added to .bash_aliases in %s's home folder.\n" %name)

bashfile = open("/home/%s/.bashrc" %name, 'a')
source = 
'''if [ -f ~/.bash_aliases ]; then
source ~/.bash_aliases
fi'''
bashfile.write(source)

aliasfile.close()
