'''
Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
'''
def main():
    f= open("filedemo.txt","a")
    #f=open("guru99-new2.txt",="a")
    for i in range(20,31):
        f.write("This is new line %d\r\n" % (i))
    f.close()
    #Open the file back and read the contents
    f=open("filedemo.txt", "r")
    if(f.mode == 'r'):
        contents =f.read()
        print(contents)
   #or, readlines reads the individual line into a list
   #fl =f.readlines()
   #for x in fl:
   #print x
    f.close()
if __name__== "__main__":
  main()