import os
langauge = input("select langauge: (kotlin,objc,swift):")
filename = f"{langauge}.py"
os.system(f"python3 {filename}")
os.system(f"python3 autoformat.py")
