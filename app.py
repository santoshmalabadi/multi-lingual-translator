from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    translation = ""

    if request.method == "POST":
        text = request.form["text"]
        language = request.form["language"]

        translation = GoogleTranslator(source='auto', target=language).translate(text)

    return render_template("index.html", translation=translation)


if __name__ == "__main__":
    app.run(debug=True)