from flask import Flask, request ,jsonify
from mongoengine import connect
from models import Song
connect('ekisde', host='mongodb://ekisde:ekisde123@ds137812.mlab.com:37812/ekisde')
app = Flask(__name__)

song= Song(title = "Symphony", author = "Clean Bandit and Sara Larzon", album = "Sympony")
song.save()
@app.route('/api/v1/',methods=['GET'])
def hello():
    return jsonify(
        [
            {
                'project':'API project in Python with Flask',
                'info':'Api developed in python with flask and mongodb'
            }
        ]
    )

if __name__ == '__main__':
    app.run(debug=True)

