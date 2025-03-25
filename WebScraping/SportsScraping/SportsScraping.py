import requests


# my api key for "The Odds"
API_KEY = "API_KEY"

# temporary value this will eventually read a response from the user
SPORT = "basketball_nba"

# the URL for the api to get data on the sports of the user's choosing
URL = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds"

# variable for the response gotten from the api call
response = requests.get(URL, 
    params = {
    'api_key': API_KEY,
    'regions': "us",
    'markets': "h2h,spreads",
    'oddsFormat': "american",
    'dateFormat': "iso",
    }
)

if response.status_code != 200:
    print(f'Failed to get odds: status_code {response.status_code}, response body {response.text}')

else:
    response_json = response.json()
    print('Number of events:', len(response_json))
    # for each event gotten from the api call:
    # print the home and away teams playing at what time
    # print every sportsbook taking bets 
    # the odds of the h2h or spread bets
    for event in response_json:
        print(f"{event['away_team']} at {event['home_team']} on {event['commence_time']}")
        # loop through the list of sportsbooks taking bets
        for book in event['bookmakers']:
            # name of current sportsbook in the loop
            sportsbook = book['title']
            # list of all prompts offered
            prompts = book['markets']
            print(f"Sportsbook: {sportsbook}")
            for prompt in prompts:
                # possible outcomes for each prompt
                outcomes = prompt['outcomes']
                if prompt['key'] == "h2h":
                    for outcome in outcomes:
                        print(f"Winner: {outcome['name']} with {outcome['price']} odds.")
                if prompt['key'] == "spreads":
                    for outcome in outcomes:
                        print(f"Winner: {outcome['name']} with a spread of {outcome['point']} with {outcome['price']} odds.")
            print("=========================================================================================")
        print("=========================================================================================")

            
            

# Check the usage quota
print('Remaining requests', response.headers['x-requests-remaining'])
print('Used requests', response.headers['x-requests-used'])