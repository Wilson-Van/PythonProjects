import requests
from bs4 import BeautifulSoup

URL = requests.get("https://sportsbook.draftkings.com/leagues/basketball/nba?category=game-lines&subcategory=game")
soup = BeautifulSoup(URL.text, "html.parser")

# find all the teams in playing
teams = soup.findAll("div", attrs={"class":"event-cell__name-text"})

for team in teams:
    print(team.text)