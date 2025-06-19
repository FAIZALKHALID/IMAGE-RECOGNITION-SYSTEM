from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        image = request.files["image"]
        image_path = os.path.join("static", image.filename)
        image.save(image_path)

        preprocessed = preprocess_image(image_path)
        preds = model.predict(preprocessed)
        results = decode_predictions(preds, top=1)[0][0]
        label = f"{results[1]} ({results[2]*100:.2f}%)"

        return render_template("index.html", label=label, image=image.filename)
    return render_template("index.html", label=None)

if __name__ == "__main__":
    app.run(debug=True)
