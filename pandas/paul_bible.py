# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:08:43 2017

@author: azazel
"""
import urllib.request
from bs4 import BeautifulSoup
counter = 1
url = r"http://www.pocbible.com/adyayam.asp?val="+str(counter)+"&book=D%C2]%AFn"
data = urllib.request.urlopen(url) 
response = data.read()
soup = BeautifulSoup(response, 'html.parser')
a = soup.find_all('font', {'class':"thiruvachanam01"})
print(a)
