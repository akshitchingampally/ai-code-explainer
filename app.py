from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://openrouter.ai/api/v1"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/explain", methods=["POST"])
def explain():
    code = request.json["code"]

    prompt = "Explain this code in simple beginner friendly words:\n" + code

    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    explanation = completion.choices[0].message.content

    return jsonify({"explanation": explanation})

if __name__ == "__main__":
    app.run(debug=True)
