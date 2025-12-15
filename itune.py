# import sys
# import json 
# import requests
# if len(sys.argv)!=2:
#     sys.exit()
#     response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#     print(response.json())
import sys
import json
import requests

if len(sys.argv) != 2:
    print("Usage: python script.py <search_term>")
    sys.exit()

# search_term = sys.argv[1]

response = requests.get(
    "https://itunes.apple.com/search",
    params={"entity": "song", "limit": 50, "term": sys.argv[1]}
)
# not user friendly looking criptic
# print(json.dumps(response.json(),indent=2))


o = response.json()
for result in o["results"]:
    print(result["trackName"])
