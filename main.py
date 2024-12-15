from api.cdragon import fetch_champs
from utils.data_parser import parse_champs

def main():
    raw_data = fetch_champs()
    if raw_data:
        champions = parse_champs(raw_data)
        for c in champions:
            print(f"{c['name']} (Cost: {c['cost']}, Traits: {', '.join(c['traits'])})")
    else:
        print("Data retrieval failure - printing from main.py")

if __name__ == "__main__":
    main()

    