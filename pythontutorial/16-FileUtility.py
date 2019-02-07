import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
def main():
# Print the name of the OS
    print("os name ", os.name)
# Check for item existence and type
    print("Item exists: " , path.exists("guru99new.txt"))
    print("Item is a file: " , path.isfile("guru99new.txt"))
    print("Item is a directory: " , path.isdir("guru99new.txt"))
# Work with file paths
    print("Item's path: " , path.realpath("guru99new.txt"))
    print("Item's path and name: " , path.split(path.realpath("guru99new.txt")))
#Get the modification time
    t = time.ctime(path.getmtime("guru99new.txt"))
    print("Modified time ", t)
    print("From time stamp ",datetime.datetime.fromtimestamp(path.getmtime("guru99new.txt")))
if __name__== "__main__":
    main()



import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main():
# make a duplicate of an existing file
    if path.exists("guru99.txt"):
# get the path to the file in the current directory
        src = path.realpath("guru99.txt");
# rename the original file
        os.rename("guru99.txt","guru99new1.txt")
# now put things into a ZIP archive
        root_dir,tail = path.split(src)
        shutil.make_archive("guru99 archive", "zip", root_dir)
# more fine-grained control over ZIP files
with ZipFile("testguru99.zip","w") as newzip:
	newzip.write("guru99.txt")
	newzip.write("guru99.bak.txt")

if __name__== "__main__":
	  main()