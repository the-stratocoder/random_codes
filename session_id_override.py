import requests

API_URL = "https://ai.voiceerp.com/api/v1/prediction/175c6dee-5166-4b24-8e6c-4cd6f2353574"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

output = query({
    "question": "Hey, do you remember my name?",
    "overrideConfig": {
        "sessionId": "42",
    }
})
