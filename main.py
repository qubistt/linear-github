import requests
import json

url = "https://api.linear.app/graphql"
headers = {
    "Content-Type": "application/json",
    "Authorization": "lin_api_HmzwFahgQjYaVp4XArtwjeUHBB0tuPn5H04NPZp7"
}
data = {
    "query": "{ me { viewer { id title } } }"
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())
