# import requests
# import json

# url = "http://192.168.233.172:3000/all"

# responseCode = requests.get(url)
# print(responseCode)
# info = json.loads(responseCode.content)
# print(info)

# import requests
# import json

# url = "http://192.168.233.172:3000/info"
# data = {
#     "name":"nitin"
# }

# response = requests.get(url, json=data, headers={"content-type":"Application/JSON"})
# print(response)
# info = json.loads(response.content)
# print(info)

import requests
import json

url = "http://192.168.233.172:3000/add"
data = {
  "name":"python",
  "age":40,
  "city":"pune",
  "steps":1500,
  "pulse":92,
  "oxygen":94,
  "temperature":98.0
}

response = requests.post(url, json=data, headers={"content-type":"Application/JSON"})
print(response)
print(response.content)
