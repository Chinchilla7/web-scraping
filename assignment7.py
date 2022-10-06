import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.ranker.com/list/medicine-used-different-things/emily-mast?ref=browse_list')
page
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')


# get the text from each repo
descriptions = soup.find_all('h2', class_='Title_title__J34jc')

#will contain info parsed from html
item_names = []
for i in descriptions:
    print (i.text)
    items = i.text
    ## clean name remove whitespace
    items = items.strip()
    ## remove new line
    items = items.replace('\n','')
    ## remove all white space
    items = items.replace(' ','')
    item_names.append(items)

len(item_names)


# get the programming language from each repo
# use attrs for items with no class
p_langauge = soup.find_all('span',attrs={'itemprop': 'programmingLanguage'})
# for each item in p_langauge, print the text
for item in p_langauge:
    print(item.text)
    da = item.text
    


# get the div that contains data-hpc
articles = soup.find_all(attrs={"data-hpc":True})  ## way one 
articles = soup.find_all('div',attrs={'data-hpc':True}) ## way two 


## put this together into a dataframe
df = pd.DataFrame({'medicine_names':item_names})

df.to_csv()

