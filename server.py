"""
server.py - Flask application for emotion detection web service.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector as detect_emotion

app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    """
    Process the POST request containing text to analyze emotions.

    Returns:
        JSON response with emotion scores and dominant emotion
        or error message for invalid input.
    """
    data = request.json
    text = data.get('text', '')

    result = detect_emotion(text)

    if result['dominant_emotion'] is None:
        return jsonify({'result': "Invalid text! Please try again!"})

    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({'result': response_str})


def main():
    """Run the Flask development server."""
    app.run(debug=True)


if __name__ == '__main__':
    main()
