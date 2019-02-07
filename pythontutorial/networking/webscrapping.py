'''
#https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
#https://stackoverflow.com/questions/12228102/how-to-install-beautiful-soup-4-with-python-2-7-on-windows
#import the library used to query a website
import urllib.request
from bs4 import BeautifulSoup
#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#Query the website and return the html to the variable 'page'
page = urllib.request('https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India')
response = page.read()
soup = BeautifulSoup(response)
print(soup.prettify())

https://www.datacamp.com/community/tutorials/web-scraping-using-python

https://realpython.com/python-web-scraping-practical-introduction/

'''
import urllib.request
from bs4 import BeautifulSoup
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India')
print("Header : ",response.info())
html = response.read()
#print("Data : ",html)
soup = BeautifulSoup(html)
print(soup.prettify())
soup.title
soup.title.string
soup.a
soup.find_all("a")




response.close()  # best practice to close the file