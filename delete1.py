# check if it exist
import os
if os.path.exists("demo2.txt"):
    os.remove("demo2.txt")
else:
    print("The file does not exist")
