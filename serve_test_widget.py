from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    rasa_url = os.environ.get('RASA_URL', 'http://rasa:5005')
    return send_from_directory('.', 'test_widget.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port) 