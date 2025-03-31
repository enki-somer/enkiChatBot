from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/webhooks/facebook/webhook', methods=['GET'])
def verify():
    """Facebook webhook verification."""
    verify_token = "test123"
    
    # Parse params from the webhook verification request
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    # Print all parameters for debugging
    print(f"Mode: {mode}")
    print(f"Token: {token}")
    print(f"Challenge: {challenge}")
    
    # Check if a token and mode were sent
    if mode and token:
        # Check the mode and token sent are correct
        if mode == 'subscribe' and token == verify_token:
            # Respond with 200 OK and challenge token
            print("WEBHOOK_VERIFIED")
            return challenge
        else:
            # Responds with '403 Forbidden' if verify tokens do not match
            print(f"Verification failed. Token mismatch: {token} != {verify_token}")
            return Response("Forbidden", status=403)
    
    return Response("Bad Request", status=400)

@app.route('/', methods=['GET'])
def hello():
    return "Hello, this is a test webhook server!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port) 