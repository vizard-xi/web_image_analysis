from flask import Flask, render_template, url_for, redirect, request
import requests
from werkzeug import secure_filename
import os


app = Flask(__name__)
    

@app.route('/')
def index():
    return render_template('home.html')
    


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/result', methods= ['GET', 'POST'])
def result():
    
    post_url = str(request.form.get('url'))
    
    image_url = post_url
    
    response = requests.post(f"https://faceplusplus-faceplusplus.p.rapidapi.com/facepp/v3/detect?image_url={image_url}",
      headers={
        "X-RapidAPI-Host": "faceplusplus-faceplusplus.p.rapidapi.com",
        "X-RapidAPI-Key": "e16b0cb017msh3716024e485f05ap18269fjsn9b2db0896d8a",
        "Content-Type": "application/x-www-form-urlencoded"
      }
        )

    api_output = response.json()
    
    
    return render_template('result.html', index = api_output)


if __name__ == "__main__":
    app.run(port = 5000,debug=True)
    
#    app.config["IMAGE_UPLOADS"] = "/home/kay/Project/static/uploads"
#        
#    if request.method == "POST":
#        
#        if request.files:
#            image = request.files["image"]
#            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
#
#            return redirect(request.url)
    

