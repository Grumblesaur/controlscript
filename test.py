import os
import sys

if sys.version_info >= (3,0):
	input = raw_input

answer = raw_input("Update system? ").lower()

if answer == "n" or answer == "no":
	sys.stdout.write("Update aborted.\n")
else:
	os.system("sudo apt-get update && sudo apt-get upgrade")

