# -*- coding: utf-8 -*-
import urllib
try:
#    url = 'https://www.google.com/search?q=python'
    url = 'https://kaushalya.tech/'
    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    print('what type', type(respData))
#    respData1 = respData)

    saveFile = open('withHeaders.txt','w')
    saveFile.write(respData.decode('ASCII'))
    saveFile.close()
except Exception as e:
    print(e)
