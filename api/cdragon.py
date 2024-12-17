import requests     # library that handles API requests

# URL that all of our urls will have
BASE_URL = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/"
current_set = 13    # current set/season number

# function that fetches champ information from CDragon API
def fetch_champs():
    path = f"{BASE_URL}v1/tftchampions-teamplanner.json"    # path to json file with champ info
    response = requests.get(path)       # response variable

    if response.status_code == 200:     # successful response from API
        champ_info = response.json()
        return champ_info.get(f"TFTSet{current_set}", [])   #extracts information under current TFT set with default val of [] if fails

    else:   # if response fails/other
        print(f"Error: API response for fetch_champs() failed - status code{response.status_code}")    # print error message
        return None
    
def fetch_image_splash(image_path):
    # image_path is the raw unedited "squareSplashIconPath" variable
    # need to make it lowercase and delete /lol-game-data/assets/ part of the path - 21 starting at 0
    image_path = image_path.lower()   # makes lowercase
    image_path = image_path[22:]    # deletes first part of path
    response = requests.get(image_path)

    if response.status_code == 200:
        image_info = response.json()
        return image_info
    else: 
        print(f"Error: API response failed for fetch_image_splash() failed - status code{response.status_code}")    # print error message
        return None


def fetch_trait_icons():
    path = "https://raw.communitydragon.org/latest/game/assets/ux/traiticons/"
    response = requests.get(path)

    if response.status_code == 200:
        trait_info = response.json()
        return trait_info
    else:   # if response fails/other
        print(f"Error: API response failed for fetch_trait_icons() failed - status code{response.status_code}")    # print error message
        return None