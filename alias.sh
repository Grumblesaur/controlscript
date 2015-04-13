# To make your life a little bit easier, I recommend making these aliases
# in your .bashrc so that you can use them in any directory.
# Of course, you'll want to substitute the "your_name/path/to/" bits with
# the actual filepath to where you cloned/forked the controlscript repo.

# Alternatively, if you're feeling bold and you have a lot of buttons on
# your keyboard, you might also consider binding the python scripts to
# keystrokes. I haven't tested if that will work, so proceed with caution.

alias commit='python /home/your_name/path/to/commit.py'
alias push='python /home/your_name/path/to/defaultpush.py'
alias pull='python /home/your_name/path/to/defaultpull.py'
alias linecount='python /home/your_name/path/to/linecount.py'

# note that while these aliases are in place, linecount.py and commit.py
# take command line arguments, after typing in the name of the alias, you'll
# need to type the appropriate arguments.
