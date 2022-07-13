from flask import Flask, render_template
import random, marvel

app = Flask(__name__)

@app.route("/")
def home():
    marvel_character = random.choice(marvel.super_heroes)
    name_desc = marvel.show_name_desc(marvel_character)
    try:
        # character_image = name_desc
        character_image = name_desc[2]['path'] + "." + name_desc[2]['extension']
        # render_template("index.html", character_name = name_desc[0], character_desc = name_desc[1])
    finally:
        # print(marvel_character)
        return render_template("index.html", character_name = name_desc[0], character_desc = name_desc[1], character_image=character_image)

if __name__ == "__main__":
    app.run(debug=True)
