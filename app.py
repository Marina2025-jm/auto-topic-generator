from flask import Flask, request, jsonify
from hot_topics import get_hot_topics

app = Flask(__name__)

@app.route('/generate-topics', methods=['POST'])
def generate_topics():
    data = request.get_json()
    prompt = data.get("prompt", "Napoléon")
    topics = get_hot_topics(prompt)
    return jsonify({"topics": topics})

if __name__ == '__main__':
    app.run(debug=True)
