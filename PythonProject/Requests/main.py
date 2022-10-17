import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 993,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "kotlovan",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.json())


response = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 993,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "brick",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.json())


response = requests.get("https://petstore.swagger.io/v2/pet/993")
print(response.json())