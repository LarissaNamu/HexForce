from api.cdragon import clean_image_path

def parse_champs(champ_data):
    champs = []
    for champ in champ_data:
        name = champ.get("display_name")
        cost = champ.get("tier")
        traits = [trait.get("name") for trait in champ.get("traits",[])]    # get the names of traits
        image_path = champ.get("squareSplashIconPath")
        image_path = clean_image_path(image_path)

        champs.append({
            "name" : name,
            "cost" : cost,
            "traits" : traits,
            "image_path" : image_path
        })
    return champs