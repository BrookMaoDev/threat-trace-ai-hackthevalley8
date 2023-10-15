from flask import Flask, render_template, request
import os

app = Flask(__name__)

folder_path = "static/images/pistols_jpgs/"
file_names = os.listdir(folder_path)

current_index = 0
current_image = folder_path + file_names[0]


@app.route("/")
def index():
    gun_exists = "Gun Exists"  # Replace with the actual text you want to pass

    return render_template(
        "index.html", gun_exists=gun_exists, image_path=current_image
    )


@app.route("/next_image", methods=["POST"])
def next_image():
    global current_image
    global current_index

    current_image = folder_path + file_names[current_index]
    current_index += 1

    return render_template(
        "index.html",
        gun_exists="Gun Exists",
        image_path=current_image,
        current_image=current_image,
    )


if __name__ == "__main__":
    app.run(debug=True)