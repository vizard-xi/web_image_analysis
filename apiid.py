import requests

#response = requests.get("https://alisamac-justvisual-garden-v1.p.rapidapi.com/api-search/by-url?url=https%3A%2F%2Finteng-storage.s3.amazonaws.com%2Fimages%2Fimport%2F2016%2F10%2Fraw-weed4.jpg",
#  headers={
#    "X-RapidAPI-Host": "alisamac-justvisual-garden-v1.p.rapidapi.com",
#    "X-RapidAPI-Key": "e16b0cb017msh3716024e485f05ap18269fjsn9b2db0896d8a"
#  }
#)
headers={
    "X-RapidAPI-Host": "alisamac-justvisual-garden-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "e16b0cb017msh3716024e485f05ap18269fjsn9b2db0896d8a"
  }

img_url= 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Cup_plant.jpg/1200px-Cup_plant.jpg'

base_service_url = "https://alisamac-justvisual-garden-v1.p.rapidapi.com/api-search/by-url"

payload = {'url': img_url, 'apikey': 'e16b0cb017msh3716024e485f05ap18269fjsn9b2db0896d8a'}

r = requests.get(base_service_url, params=payload, headers=headers)

print(r)

'''response = unirest.get("https://alisamac-justvisual-garden-v1.p.rapidapi.com/api-search/by-url",
  headers={
    "X-RapidAPI-Host": "alisamac-justvisual-garden-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
  }
)'''