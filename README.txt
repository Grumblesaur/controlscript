TABLE OF CONTENTS

010 :: LICENSING INFORMATION

100 :: DEPENDENCES
110 :: DISCLAIMERS	

200 :: push.py
210 :: pull.py
215 :: NOTE
220 :: commit.py
230 :: linecount.py
240 :: user.py

010 :: LICENSING INFORMATION
    controlscript package: simple tools for managing a project directory
    Copyright (C) 2015  James Murphy

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
    
    (See LICENSE.md for additional details)
    
100 :: DEPENDENCIES
  The commit.py, push.py, and pull.py scripts expect to be run in a git
  repository, and as such require git to be installed. Naturally, of course,
  you'll need to have Python installed as well, but if you hadn't figured
  that out already, I'd be curious as to why you're even still scrolling
  through this README.

  The controlscript package is designed to be version agnostic. That is,
  it will function with the latest versions of Python 2 and Python 3.

110 :: DISCLAIMERS
  I have designed this package in and for a Unix-like environment. If you
  have any wish to use this package of scripts in a Windows environment,
  you're on your own.
  
200 :: push.py
  Running "push" in a Github repo will prompt you for some abbreviated input
  to push to "origin" or "upstream" more quickly. Pushing elsewhere will
  require you to edit the push.py script or manually use the git commands
  themselves. This script is purely for convenience.
  
  It also defaults pushing to master of whatever destination was initially
  given, but branch can be specified by the user.
  
  
210 :: pull.py
  Running "pull" is similar to running "push" -- it's just a mechanism for
  streamlining the process of interfacing git. If you want additional
  functionality, you'll need to add to it yourself, unless I find myself
  personally needing more out of it.
  
215 :: NOTE
  The "push" and "pull" scripts expect you to have already added remote
  destinations to push and pull to with git itself. To reiterate, they
  are merely wrapper processes to reduce the overhead of dealing with
  git.
  
220 :: commit.py
  The "commit" script takes command line input, expecting file extensions
  of all the types of files you want added to your git repo. It will also
  automatically attempt to add a Makefile if it exists. Once all the files
  with the specified extensions have been added, it will automatically begin
  the commit process.
  
230 :: linecount.py
  The "linecount" script will take any number of filenames passed as
  arguments and attempt to count the number of lines of code, comments, and
  whitespace in each string. Files that do not have a recognized file
  extension will prompt the user to add the file extensions to the file
  'styles.txt'.
  
  The output of "linecount" is a file with the linecounts for each
  individual file as well as a summary of all the files at the end of the
  file.
  
240 :: user.py
  Here the user specifies the name of their preferred text editor in Linux
  and the location of where they forked/cloned this Github repo.
  
  This information is used by the "linecount" script.
