from flask import Flask, render_template, session
import requests
import json
import os
import random

app = Flask(__name__)
app.secret_key = "sdjfrsl;avnyfvea"

@app.route('/', methods=['GET', 'POST'])
def m():
    r = requests.post("https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=3db17d7eb428d1c764eed5f83dd509bc&tags=travel&format=json&accuracy=6&has_geo=1&nojsoncallback=?").json()["photos"]

    photo = random.choice(r["photo"])
    session['p_id'] = photo["id"]
    return render_template('index.html', link="https://live.staticflickr.com/7372/{0}_{1}_z.jpg".format(photo["id"], photo["secret"]))

@app.route('/guess', methods=['POST'])
def g():
    print(session['p_id'])
    r = requests.post("https://api.flickr.com/services/rest/?method=flickr.photos.geo.getLocation&api_key=3db17d7eb428d1c764eed5f83dd509bc&photo_id={0}&format=json&nojsoncallback=?".format(session['p_id'])).json()
    print(r)
    return json.dumps({"coords":[r["photo"]["location"]["latitude"], r["photo"]["location"]["longitude"]]})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))