import os
path_dir = './'
files = os.listdir(path_dir)
for file in files:
    filename, ext = file.split(".")
    if ext == "py":
        # brew install astyle (http://astyle.sourceforge.net/astyle.html#_Quick_Start)
        # os.system(f"astyle --style=google {file}")

        # brew install astyle (http://astyle.sourceforge.net/astyle.html#_Quick_Start)
	    break
    elif ext == "h" or ext =="m":
        # clang format
        os.system(f"clang-format -i {file}")
    elif ext == "kt":
        os.system(f"ktlint -F {file}")
    else:
        os.system(f"echo -e 'G=gg\n:wq\n' | vim {file}")

