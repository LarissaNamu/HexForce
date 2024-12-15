import requests     # library that handles API requests

# URL that all of our urls will have
BASE_URL = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/"
current_set = 13    # current set/season number

# function that fetches champ information from CDragon API
def fetch_champs():
    path = f"{BASE_URL}v1/tftchampions-teamplanner.json"    # path to json file wtih champ info
    response = requests.get(url)       # response variable

    if response.status_code == 200:     # successful response from API
        champ_info = response.json()
        return champ_info.get(f"TFTSet{current_set}", [])   #extracts information under current TFT set with default val of [] if fails

    else:   # if response fails/other
        print(f"Error: API response failed - status code{response.status_code}")    # print error message
        return None