#https://zonacoding.com/article/penerapan-mvc-di-flask-python

from flask import Flask ## import Flask dari package flask

app = Flask(__name__)

app.static_folder = 'static'

from app.controllers import  *