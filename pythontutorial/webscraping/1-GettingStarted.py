import requests
from bs4 import BeautifulSoup
# Collect and parse first page
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')
#print('artist list #',artist_name_list)

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')
#print('artist link', artist_name_list_items)

# Create for loop to print out all artists' names
#for artist_name in artist_name_list_items:
    #print(artist_name.prettify())
    # Use .contents to pull out the <a> tag’s children
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    print(names)
    links = 'https://web.archive.org' + artist_name.get('href')
    print(links)