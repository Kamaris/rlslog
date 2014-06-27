#!/usr/bin/python

from bs4 import BeautifulSoup as BS

soup = BS(open("index.html"))
soup.prettify()

soup = soup.find(id="content")
#soup = soup.encode('utf-8')

#soup = BeautifulSoup(soup)

print(soup)

#print soup.find(id="content")
#print soup.find_all('a')
#print(soup.get_text())

#for link in soup.find_all('a'):
#    print(link.get('href'))
