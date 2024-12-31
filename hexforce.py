from api.cdragon import fetch_champs
from utils.data_parser import parse_champs
from utils.tft_objects import Champions, Teams
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee2e16f4947fa139c92504e7edae21ab'

raw_data = fetch_champs()

champions_list = []     # after for loop ends, this array contains all of the tft's set's champs in champion form
if raw_data:
    champs = parse_champs(raw_data)
    for c in champs:
        # create champ object and append to champion list
        temp_champ = Champions(c['name'], c['cost'], c['traits'], c['image_path'])
        print(temp_champ.image_path)    #delete after testing
        champions_list.append(temp_champ)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', champions = champions_list, title = "Home")

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)