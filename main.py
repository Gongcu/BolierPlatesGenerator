import os
langauge = input("select langauge: (kotlin,objc,swift):")
filename = f"{langauge}.py"
crud = input("select command - crud (eg. cr):")
os.system(f"python3 {filename} {crud}")
os.system(f"python3 autoformat.py")
