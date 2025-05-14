from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual SwiftChat bot token
SWIFTCHAT_BOT_TOKEN = "Bearer 21bda582-e8d0-45bc-bb8b-a5c6c555d176"
SWIFTCHAT_API_URL = "https://v1-api.swiftchat.ai/api/bots/0233593561541825/messages"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(type(data))
    print("data: " + str(data))

    user_message = data.get('type', {}).strip().lower()
    user_id = data.get('from')  # This is the recipient of your bot's message

    if user_message.lower() in ['text']:
    	send_swiftchat_message(data, "Welcome!")
    	send_button_message()


    if user_message in ['button_response']:
    	call_backend(data.get('text', {}).get('body', '').strip().lower())
	

    return jsonify({"status": "ok"}), 200

def send_swiftchat_message(to, message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": SWIFTCHAT_BOT_TOKEN
    }
    payload = {
        "to": "+918010562733",
        "type": "text",
        "text": {
            "body": "Hi, Welcome User!"
        }
    }

    response = requests.post(SWIFTCHAT_API_URL, headers=headers, json=payload)
    
    print("Sent message:", response.status_code, response.text)
    
def send_swiftchat_language(to, message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": SWIFTCHAT_BOT_TOKEN
    }
    payload = {
        "to": "+918010562733",
        "type": "text",
        "text": {
            "body": """This will invoke our backend function to provide history of the day based on selected language
            
            +---------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Year    | Event                                                                                                                                                      |
+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 49 BC   | Julius Caesar crosses the Rubicon, signalling the start of civil war.                                                                                     |
| 9       | The Western Han dynasty ends when Wang Mang claims that the divine Mandate of Heaven called for the end of the dynasty and the beginning of his own ...  |
| 69      | Lucius Calpurnius Piso Licinianus is appointed by Galba as deputy Roman Emperor.                                                                          |
+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------+"""
        }
    }

    response = requests.post(SWIFTCHAT_API_URL, headers=headers, json=payload)
    
    print("Sent message:", response.status_code, response.text)

def send_button_message():
    headers = {
        "Content-Type": "application/json",
        "Authorization": SWIFTCHAT_BOT_TOKEN
    }

    payload = {
        "to": "+918010562733",
        "type": "button",
        "button": {
            "body": {
                "type": "text",
                "text": {
                    "body": "Please select your language"
                }
            },
            "buttons": [
                {
                    "type": "solid",
                    "body": "English",
                    "reply": "English"
                },
                {
                    "type": "solid",
                    "body": "Spanish",
                    "reply": "Spanish"
                }
            ],
            "allow_custom_response": False
        },
        "rating_type": "thumb"
    }

    response = requests.post(SWIFTCHAT_API_URL, headers=headers, json=payload)

def call_backend(data):
	send_swiftchat_language(data, "Welcome!")
	
	
@app.route('/', methods=['GET'])
def health_check():
    return "Bot is running", 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)