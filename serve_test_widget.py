from flask import Flask, render_template, send_from_directory, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    with open('test_widget.html', 'r') as file:
        html_content = file.read()
    
    # Replace placeholder with actual RASA_URL from environment variable
    rasa_url = os.environ.get('RASA_URL', 'http://localhost:5005')
    html_content = html_content.replace('process.env.RASA_URL || \'http://localhost:5005\'', f'"{rasa_url}"')
    
    return html_content, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port) 