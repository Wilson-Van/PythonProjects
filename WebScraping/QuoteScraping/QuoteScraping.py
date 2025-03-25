from bs4 import BeautifulSoup
import requests
import csv

# create a request call to get the url for where we want to scrape
scrape_location = requests.get("https://quotes.toscrape.com/")
# parse the html contents using the BeautifulSoup library
soup = BeautifulSoup(scrape_location.text, "html.parser")
# because the quotes are all tagged as span and have a class of text
# we can just find all that fit that description and add it to a list called quotes
quotes = soup.findAll("span", attrs={"class":"text"})
# the same logic can be used for the authors as they are all tagged with small and a class of author
authors = soup.findAll("small", attrs={"class":"author"})

# this will open a csv file to write to encoding using utf-8 in case of special characters
file = open("./scraped_quotes.csv", 'w', encoding="utf-8")
writer = csv.writer(file)
# I want to format the csv file a little better so I made a title for each row.
writer.writerow(["QUOTES", "AUTHORS"])


# for loop to loop through each quote and author
for quote, author in zip(quotes, authors):
    # write the quote in a  row and then the author in the next
    writer.writerow([quote.text, author.text])

# close the file
file.close()
