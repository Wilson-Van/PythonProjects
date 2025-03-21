# QuoteScraping

## Description:

This is a simple program that will take the quotes from a website ("https://quotes.toscrape.com/") and get the information on certain texts to get the quote and author of said quote. I will be following a tutorial (https://www.youtube.com/watch?v=QhD015WUMxE&t=209s) to become familiar with the tools I will be using and then I will apply the lessons I have learned to other projects I will be doing with the same tools. I will comment each line of code to understand what the code is doing rather than blindly following the tutorial.

## Tools:

I will be using multiple different libraries which I will be installing with pip. The libraries I will be using are requests, bs4 (BeautifulSoup), and csv.

## Resources:

As I said before I will be following a tutorial for this project to simply learn the tools of web scraping. The tutorial is callled, "Beginners Guide To Web Scraping with Python - All You Need To Know" by Tinkernut which can be found at https://www.youtube.com/watch?v=QhD015WUMxE&t=209s. I will be scraping from "https://quotes.toscrape.com/" to avoid any legal or ethical dilemmas as this website was made to test scrapers.

## Output:

After running the python script the resulting csv file should be the same as the "scraped_quotes.csv" file found in this folder.

## Issues:

Currently the only issue I ran into is that certain characters were not displaying properly after doing a little bit of research I found I had to using 'encoding = "utf-8"' so certain characters would display as shown. However after doing so some of the quotes are now double quoted. I did a little bit of research and just found that it is a formatting issue with certain softwares such as excel. This isn't a major bug so I will not spend anymore time to fix it, however, if I were to fix it I would probably just strip the quotes of there quotation marks and manually put them back when adding them to the rows in the csv.