from flask import Flask, render_template, session, jsonify
import os
import flickr

app = Flask(__name__)
app.secret_key = "set_your_key_here"


@app.route('/', methods=['GET'])
def index():
    photo = flickr.getRandomPhoto()
    session['pictureId'] = photo['id']
    return render_template('index.html', link=photo['rawLink'])

@app.route('/guess', methods=['POST'])
def guess():
    location = flickr.getPhotoCoordiantes(session['pictureId'])
    return jsonify(location)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))