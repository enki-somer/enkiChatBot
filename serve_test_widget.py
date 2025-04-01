from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def serve_widget():
    return send_file('test_widget.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port) 