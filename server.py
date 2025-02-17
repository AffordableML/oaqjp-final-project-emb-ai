from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetecor():
    result = emotion_detection.emotion_detector(request.args.get("textToAnalyze"))
    print(result)
    return result['dominant_emotion']

if __name__ == "__main__":
    app.run(port=5000)