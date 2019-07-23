import requests

image_url = "https://media.virginradio.fr/article-3374491-facebook-f1478942721/queen-l-enregistrement-premiere-session-radio.jpg"


resquest = requests.post(f"https://faceplusplus-faceplusplus.p.rapidapi.com/facepp/v3/detect?image_url={image_url}",
  headers={
    "X-RapidAPI-Host": "faceplusplus-faceplusplus.p.rapidapi.com",
    "X-RapidAPI-Key": "e16b0cb017msh3716024e485f05ap18269fjsn9b2db0896d8a",
    "Content-Type": "application/x-www-form-urlencoded"
  }
)



print(list(resquest))


#response = requests.post(f"https://faceplusplus-faceplusplus.p.rapidapi.com/facepp/v3/detect?image_url={image_url}",
#  headers={
#    "X-RapidAPI-Host": "faceplusplus-faceplusplus.p.rapidapi.com",
#    "X-RapidAPI-Key": "e16b0cb017msh3716024e485f05ap18269fjsn9b2db0896d8a",
#    "Content-Type": "application/x-www-form-urlencoded"
#  }
#)
#
#print(list(response))


