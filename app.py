from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
    

@app.route('/')
def index():
    image_url = "https://www.sbs.com.au/topics/sites/sbs.com.au.topics/files/197886641.jpg"
    response = requests.post(f"https://faceplusplus-faceplusplus.p.rapidapi.com/facepp/v3/detect?image_url={image_url}",
      headers={
        "X-RapidAPI-Host": "faceplusplus-faceplusplus.p.rapidapi.com",
        "X-RapidAPI-Key": "e16b0cb017msh3716024e485f05ap18269fjsn9b2db0896d8a",
        "Content-Type": "application/x-www-form-urlencoded"
      }
        )
    
#    print(response.text)

    r = response.json()

#    print(dict(r))


    return render_template('home.html', index = r)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

