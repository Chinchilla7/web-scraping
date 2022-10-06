Packages needed for this repo are beautfiulsoup from bs4, pandas, and requests.

Using beautifulsoup to perform different search functionalities on the html we pulled from the get request.

soup.find_all is a function of beautiful soup that searches through the entire html file for the 2 arguments: tag name and class, 
returning all data with those parameters.

We can use attrs= for special cases in which there are no class for the data item, but a custom name.

The tags and class we used to extract info from the two sites were: 'h2', class_='Title_title__J34jc' and 'h2'.

With the function: 'for x in y:
    print(x.text)', for each item in the y we print the text only.

We create an empty list Var [] for each site, and at the end of the prior function do 
an .append() to put all the clean info into the list.

