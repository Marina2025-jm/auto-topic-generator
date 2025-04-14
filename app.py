from flask import Flask, request, jsonify
from hot_topics import get_hot_topics
import os  # ✅ 必须加上这行

app = Flask(__name__)

@app.route('/generate-topics', methods=['POST'])
def generate_topics():
    data = request.get_json()
    prompt = data.get("prompt", "Napoléon")
    topics = get_hot_topics(prompt)
    return jsonify({"topics": topics})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

