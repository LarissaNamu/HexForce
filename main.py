from api.cdragon import fetch_champs
from utils.data_parser import parse_champs
from utils.tft_objects import Champions, Teams

def main():
    raw_data = fetch_champs()

    champions_list = []
    if raw_data:
        champs = parse_champs(raw_data)
        for c in champs:
            # create champ object and append to champion list
            temp_champ = Champions(c['name'], c['cost'], c['traits'], c['image_path'])
            champions_list.append(temp_champ)

            # print out the champ appended
            print(temp_champ)
        print()
        print("Now testing Teams Class:")
        my_champs = [champions_list[0], champions_list[1], champions_list[2], champions_list[4]]
        my_team = Teams("Tester Team", my_champs)
        print(my_team)

    else:
        print("Data retrieval failure - printing from main.py")

if __name__ == "__main__":
    main()

    