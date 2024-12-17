from api.cdragon import fetch_champs, fetch_trait_icons, fetch_image_splash
from utils.data_parser import parse_champs
from utils.tft_objects import Champions, Teams
from flask import Flask, render_template
app = Flask(__name__)

raw_data = fetch_champs()

champions_list = []     # after for loop ends, this array contains all of the tft's set's champs in champion form
if raw_data:
    champs = parse_champs(raw_data)
    for c in champs:
        # create champ object and append to champion list
        temp_champ = Champions(c['name'], c['cost'], c['traits'], c['image_path'])
        champions_list.append(temp_champ)

# retrieve images of the champions
image_list = []
for c in champions_list:
    path = c.get_image_path()
    raw_image = fetch_image_splash(path)
    image_list.append(raw_image)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', champions = champions_list, title = "Home")

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

if __name__ == '__main__':
    app.run(debug=True)