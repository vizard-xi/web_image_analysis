from flask import Flask, render_template, url_for, redirect, request
import requests
from werkzeug import secure_filename
import os


app = Flask(__name__)
    

@app.route('/', methods= ['GET', 'POST'])
def index():
    
    app.config["IMAGE_UPLOADS"] = "/home/kay/Project/static/uploads"
        
    if request.method == "POST":
        
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            return redirect(request.url)
    
    
    image_url = ''
    
    response = requests.post(f"https://faceplusplus-faceplusplus.p.rapidapi.com/facepp/v3/detect?image_url={image_url}",
      headers={
        "X-RapidAPI-Host": "faceplusplus-faceplusplus.p.rapidapi.com",
        "X-RapidAPI-Key": "e16b0cb017msh3716024e485f05ap18269fjsn9b2db0896d8a",
        "Content-Type": "application/x-www-form-urlencoded"
      }
        )

    r = response.json()

    return render_template('home.html', index = r)
    


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(port = 5000,debug=True)

