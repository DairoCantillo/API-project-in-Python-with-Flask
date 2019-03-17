from flask import Flask, request ,jsonify
from mongoengine import connect
from models import Song
import spotipy
connect('ekisde', host='mongodb://ekisde:ekisde123@ds137812.mlab.com:37812/ekisde')
app = Flask(__name__)

Song(title = "tongowouky", author = "tongo", album = "yea yea").save()
@app.route('/',methods=['GET'])
def hello():
    return jsonify(
        [
            {
                'project':'API project in Python with Flask',
                'info':'Api developed in python with flask and mongodb'
            }
        ]
    )

@app.route('/api/v1/data/songs/all', methods=['GET'])
def send_songs():
    all_songs = Song.objects
    all_songs_json = [s.to_dict() for s in all_songs]
    return jsonify(all_songs_json)


if __name__ == '__main__':
    app.run(debug=True)

