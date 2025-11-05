import requests

session_id = None
BASE_URL = "http://127.0.0.1:8000/chat"

# Start chat (get greeting)
response = requests.post(BASE_URL, json={"message": "", "session_id": session_id}).json()
session_id = response["session_id"]
print("Bot:", response["reply"])

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = requests.post(BASE_URL, json={"message": user_input, "session_id": session_id}).json()
    session_id = response["session_id"]
    print("Bot:", response["reply"])
