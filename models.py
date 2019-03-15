from mongoengine import *
import datetime

class Song(Document):
    title = StringField(max_lenth=200, required=True)
    author = StringField(max_lenth=100, required=True)
    album = StringField(max_lenth=50, required=True)
