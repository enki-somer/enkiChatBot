from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello, this is a test webhook server!"

@app.route('/test', methods=['GET'])
def test():
    # Get query parameters
    hub_mode = request.args.get('hub.mode', '')
    hub_token = request.args.get('hub.verify_token', '')
    hub_challenge = request.args.get('hub.challenge', '')
    
    print(f"Mode: {hub_mode}")
    print(f"Token: {hub_token}")
    print(f"Challenge: {hub_challenge}")
    
    # Simple verification - always succeeds
    if hub_challenge:
        return hub_challenge
    
    return "Test endpoint is working!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port) 