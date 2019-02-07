#import urllib.request
'''
import urllib.parse

x = urllib.request.urlopen('https://www.google.com/')
x.useragent()
print(x.read())


try:
    x = urllib.request.urlopen('https://kaushalya.tech/')
    #print(x.read())
    saveFile = open('noheaders.txt','w')
    saveFile.write(x.read())
    saveFile.close()
except Exception as e:
    print(e)
'''
import urllib.request
import urllib.parse
try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))


'''

print('search google')
url = 'https://www.google.com/search'
values = {'q' : 'python programming tutorials'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''