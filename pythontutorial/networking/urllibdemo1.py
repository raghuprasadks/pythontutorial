import urllib.request
response = urllib.request('https://www.pythonforbeginners.com/')
print("Header : ",response.info())
html = response.read()
print("Data : ",html)
response.close()  # best practice to close the file
