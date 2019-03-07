# -*- coding: utf-8 -*-
#pip install bs4
from bs4 import BeautifulSoup
html_doc = """
<!DOCTYPE html>
<html>
<head>
	<title>Web Scraping Sample</title>
</head>
<body>
	<div id="section-1">
		
		<h3 data-hello="hi">Hello</h3>
		<img src="https://source.unsplash.com/1600x900/?nature,water">
		<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
		proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
	</div>
	<div id="section-2">
		<ul class="items">
			<li class="item"><a href="#">Item 1</a></li>
			<li class="item"><a href="#">Item 1</a></li>
			<li class="item"><a href="#">Item 2</a></li>
			<li class="item"><a href="#">Item 3</a></li>
			<li class="item"><a href="#">Item 4</a></li>
			<li class="item"><a href="#">Item 5</a></li>
		</ul>
	</div>

</body>
</html>
"""
soup = BeautifulSoup(html_doc,'html.parser')
#Direct
#print(soup.body)
#print(soup.head)
#print(soup.head.title)

#find()
el = soup.find('div')
#print(el)
el = soup.find_all('div')
el = soup.find_all('div')[1]
el = soup.find(id='section-1')
el = soup.find(class_='items')
el = soup.find(attrs={"data-hello":"hi"})
el=soup.select('#section-1')
el=soup.select('.item')[0]
el=soup.find(class_='item').get_text()
for item in soup.select('.item'):
    print('test')
#    print(item.get_text())

# Navigation
#el = soup.body.contents[1].contents[1].find_next_sibling()
#print(soup.body.contents[1].contents[1].find_next_sibling())
#el =soup.find(class_='item').find_parent()
el=soup.find('h3').find_next_sibling('p')
print(el)