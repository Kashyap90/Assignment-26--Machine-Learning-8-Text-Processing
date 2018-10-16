
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import urllib.request
import re


# In[9]:


response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html, "html5lib")
#print(soup.text)
snow_soup = BeautifulSoup(soup.text, 'html.parser')

print(snow_soup)
soup.findAll('a')[:12] 
text = soup.getText() 
print(text) 


# In[4]:


tokens = re.findall('\w+',text)
tokens[:10]


# In[5]:


word_count = []
for word in tokens:
    word_count.append(word)
    
word_count[:5]


# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns
import nltk

get_ipython().run_line_magic('matplotlib', 'inline')

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set_style('darkgrid')

nlp_words = nltk.FreqDist(word_count)
nlp_words.plot(20)

