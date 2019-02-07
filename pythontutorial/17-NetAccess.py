#
# read the data from the URL and print it --- Not working
#


'''
import urllib2
def main():
    # open a connection to a URL using urllib2
    webUrl = urllib.urlopen("https://www.youtube.com/user/guru99com")

    # get the result code and print it
    print("result code: " + str(webUrl.getcode()))

    # read the data from the URL and print it
    data = webUrl.read()
    print(data)


if(__name__ == "__main__"):
    main()
 '''

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   c.send('Thank you for connecting')
   c.close()                # Close the connection