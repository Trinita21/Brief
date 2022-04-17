from flask import Flask, render_template, url_for
import requests
from flask import request
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/Summarization', methods=['GET', 'POST'])
def Summarization():
    if request.method == 'POST':
        data = request.form['data']
        min = 50
        max = 250

        # max=int(request.form['max'])
        # min=max//4

        payload = {
            "inputs": data,
            "parameters": {"min_length": min, "max_length": max},
        }
        headers = {
            "Authorization": "Bearer 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"}
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        response = requests.post(API_URL, headers=headers, json=payload)
        output = response.json()
        return render_template('index.html', result=output)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
