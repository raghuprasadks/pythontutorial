import urllib.request
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    #print(x.read())

    saveFile = open('noheaders.txt','w')
    saveFile.write(str(x.read()))
    saveFile.close()
except Exception as e:
    print(str(e))