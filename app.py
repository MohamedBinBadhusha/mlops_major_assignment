import numpy as np
from flask import Flask, request, render_template
import joblib
from PIL import Image
import io

app = Flask(__name__)

# Load the trained model
model = joblib.load("savedmodel.pth")

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('L')  # Convert to grayscale
    image = image.resize((64, 64))  # Resize to 64x64
    image = np.array(image)
    image = image.flatten().reshape(1, -1)  # Flatten to match model input
    return image

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        if "image" not in request.files:
            return "No image uploaded!", 400
        file = request.files["image"]
        img_bytes = file.read()
        processed_img = preprocess_image(img_bytes)
        prediction = model.predict(processed_img)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
