from flask import Flask,request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.utils.all_utils import decodeImage
from mit_predict import mitinside

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = mitinside(self.filename)

@app.route("/", methods = ['GET'])
@cross_origin()
def home():
    return render_template("index.html")



@app.route("/predict",methods = ["POST"])
@cross_origin()
def predictRoute():
    image = request.json["image"]
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictionmitinside()
    return jsonify(result)

clApp = ClientApp()
if __name__ == "__main__":
    app.run(debug = True, port =8000)

