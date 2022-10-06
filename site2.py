import pandas as pd
import requests
from bs4 import BeautifulSoup

page2 = requests.get('https://wildlifetrip.org/different-types-of-bears/')
page2

# Create a BeautifulSoup object
soup = BeautifulSoup(page2.text, 'html.parser')

ranking = soup.find_all('h2')

bear_names = []
for t in ranking: 
    print (t.text)
    titles = t.text
    ## clean name remove whitespace
    titles = titles.strip()
    ## remove new line
    titles = titles.replace('\n','')
    titles
    ## remove all white space
    titles = titles.replace(' ','')
    bear_names.append(titles)

#check number of items
len(bear_names)


## put this together into a dataframe
df = pd.DataFrame({'bears':bear_names})

df.to_csv()
