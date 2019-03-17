from mongoengine import *
import datetime
#canciones
class Song(Document):
    title = StringField(max_lenth=200, required=True)
    author = StringField(max_lenth=100, required=True)
    album = StringField(max_lenth=50, required=True)
    meta = {'collection' : 'songs'}
    def to_dict(self):
        data = {
            #'id' : self.Song_id,
            'title':self.title,
            'author':self.author,
            'album':self.album
        }
        return data




