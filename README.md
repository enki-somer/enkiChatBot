# Kurdish Chatbot with Rasa

A chatbot built with Rasa that collects user information in Kurdish language and integrates with Facebook Messenger.

## Features

- Responds to users in Kurdish language
- Collects user information (name, phone number, address)
- Stores collected information in a JSON file
- Ready for Facebook Messenger integration

## Project Structure

```
.
├── actions/
│   └── actions.py           # Custom actions for storing user data
├── data/
│   ├── nlu/
│   │   └── nlu.yml          # NLU training data
│   ├── rules/
│   │   └── rules.yml        # Rules for specific conversation patterns
│   └── stories/
│       └── stories.yml      # Training stories for conversation flows
├── config.yml               # Configuration for NLU and Core models
├── credentials.yml          # Credentials for connecting to messaging platforms
├── domain.yml               # Domain definition with intents, entities, slots, actions
├── endpoints.yml            # Endpoints for connecting to action server
└── README.md                # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.8+ installed
- pip (Python package installer)

### Installation

1. Create a virtual environment (recommended):

```bash
python -m venv venv
```

2. Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install Rasa and dependencies:

```bash
pip install rasa rasa-sdk
```

### Training the Bot

1. Train the Rasa model:

```bash
rasa train
```

### Running the Bot

1. Start the Rasa action server (in a separate terminal):

```bash
rasa run actions
```

2. Start the Rasa server:

```bash
rasa run --enable-api --cors "*" --debug
```

3. To test the bot locally using the Rasa shell:

```bash
rasa shell
```

## Facebook Messenger Integration

To connect your bot to Facebook Messenger:

1. Create a Facebook page and app in the Facebook Developer Portal
2. Setup a webhook for your app
3. Update the `credentials.yml` file with your Facebook app credentials:

   - Replace `YOUR_FB_SECRET` with your Facebook App Secret
   - Replace `YOUR_FB_PAGE_ACCESS_TOKEN` with your Page Access Token

4. Start your Rasa server with the following command:

```bash
rasa run --credentials credentials.yml --enable-api --cors "*"
```

## Customization

### Adding New Intents and Responses

1. Add new intents in `data/nlu/nlu.yml`
2. Add corresponding responses in `domain.yml`
3. Update stories in `data/stories/stories.yml`
4. Retrain the model with `rasa train`

### Modifying the Data Storage

The bot currently stores user data in a JSON file. To modify:

1. Edit the `action_store_user_data` action in `actions/actions.py`
2. Restart the action server

## Debugging

If you encounter issues:

1. Check the Rasa server and action server logs
2. Verify that all necessary services are running
3. Confirm that the Facebook credentials are correctly configured
4. Run `rasa data validate` to check for issues in your training data

## Additional Resources

- [Rasa Documentation](https://rasa.com/docs/rasa/)
- [Facebook Messenger Integration Guide](https://rasa.com/docs/rasa/connectors/facebook-messenger/)
- [Rasa Community Forum](https://forum.rasa.com/)
