import sys

command = sys.argv[1]; #crud
create_command = "c"
read_command = "r"
delete_command = "d"

def create():
	if create_command in command:
		return True
	else:
		return False

def read():
	if read_command in command:
		return True
	else:
		return False

def delete():
	if delete_command in command:
		return True
	else:
		return False
