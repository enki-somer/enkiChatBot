import json
import os
import datetime
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionStoreUserData(Action):
    """Custom action to store user information in a JSON file."""

    def name(self) -> Text:
        return "action_store_user_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get slot values
        name = tracker.get_slot("name")
        phone = tracker.get_slot("phone")
        address = tracker.get_slot("address")
        
        # Prepare user data
        user_data = {
            "name": name,
            "phone": phone,
            "address": address,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        # Create file path
        file_path = "user_data.json"
        
        # Load existing data if file exists
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = []
            except Exception:
                data = []
        else:
            data = []
        
        # Append new user data
        data.append(user_data)
        
        # Save updated data
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                
            dispatcher.utter_message(text=f"زانیاریەکانت بە سەرکەوتوویی تۆمار کران.")
        except Exception as e:
            dispatcher.utter_message(text=f"ببورە، کێشەیەک هەبوو لە تۆمارکردنی زانیاریەکانت: {str(e)}")
        
        return [] 