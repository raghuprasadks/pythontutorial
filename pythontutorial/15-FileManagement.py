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
    #f= open("guru99-new.txt","w+")
    f=open("guru99-new2.txt",="a")
    for i in range(40,50):
        f.write("This is new line %d\r\n" % (i+1))
    f.close()
    #Open the file back and read the contents
    f=open("guru99-new2.txt", "r")
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