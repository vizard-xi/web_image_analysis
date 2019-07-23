import requests

#response = requests.get("https://alisamac-justvisual-garden-v1.p.rapidapi.com/api-search/by-url?url=https%3A%2F%2Finteng-storage.s3.amazonaws.com%2Fimages%2Fimport%2F2016%2F10%2Fraw-weed4.jpg",
#  headers={
#    "X-RapidAPI-Host": "alisamac-justvisual-garden-v1.p.rapidapi.com",
#    "X-RapidAPI-Key": "e16b0cb017msh3716024e485f05ap18269fjsn9b2db0896d8a"
#  }
#)

r = requests.get("https://faceplusplus-faceplusplus.p.rapidapi.com/facepp/v3/detect")

print(r)