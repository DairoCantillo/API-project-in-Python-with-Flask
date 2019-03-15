from flask import Flask, request ,jsonify
from mongoengine import connect
connect('ekisde', host='mongodb://ekisde:ekisde123@ds137812.mlab.com:37812/ekisde')
app = Flask(__name__)
@app.route('/api/v1/',methods=['GET'])
def hello():
    return jsonify(
        [
            {
                'project':'API project in Python with Flask'
            }
        ]
    )

if __name__ == '__main__':
    app.run(debug=True)

