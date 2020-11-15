from flask import Flask, render_template, url_for
from app import app
#from app.models.user import User ## import kelas User dari model

#@app.route('/', methods = ['GET'])
#def index():
	#user =  User() ## membuat objek dari kelas user
	#nama = user.getName() ## memanggil method untuk mengambil nama
	#return render_template('index.html', nama=nama)

@app.route('/')
def index():
	return render_template('index2.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/login')
def login():
	return render_template('login.html')


if __name__== '__main__':
    app.run()


