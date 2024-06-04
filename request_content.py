from cleantalk import CleanTalk
import requests
import json

# Replace with your Discord webhook URL
webhook_url = 'your_discord_webhook_url'

ct = CleanTalk(auth_key='your_auth_key')
ct_result = ct.request(
                message = 'test message', # Required. Visitor comment
                sender_ip = '127.0.0.1', # Required. Visitor IP address
                sender_email = 'stop_email@example.com', # Required. Visitor email
                sender_nickname = 'spam_bot', # Required. Visitor nickname
                post_info= json.dumps({'post_url': 'https://yoursite.com'}) # Optional. Additional post info in JSON format.
                # event_token = 'xxx' # fill it with ct_bot_detector_event_token hidden input from your form (auto generate)
        )

# Convert the CleanTalk result to a string for the content field
content = f"CleanTalk Result: {json.dumps(ct_result)}"

# Your JSON payload with the content field
data = {
    "content": content
}

# Headers (optional)
headers = {
    'Content-Type': 'application/json'
}

# Send the POST request
response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

# Check the response
if response.status_code == 204:
    print("Message sent successfully")
else:
    print(f"Failed to send message: {response.status_code}, {response.text}")
