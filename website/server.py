from bottle import route, run, template, request, static_file, get, post, response, redirect, error, debug
import bottle
import sqlite3
from paste import *

# bottle.TEMPLATE_PATH.insert(0,'./views/posts')

@route('/')
def home():
	return template('home')
@route('/jsonData')
def jsonData():
	return {"name" : "jsonData", "myList" : [1,2,3,4,5]}

# blog

@route('/intro')
def intro():
	return template('intro')

@route('/talks')
def talk():
	return template('talks')

@route('/osintSlides')
def talk():
	return template('osintSlides')

@route('/resourcePage')
def resources():
	return template('resourcePage')

@route('/blogs')
def blogs():
 	return template('blogs')

@route('/blogOne')
def blogOne():
 	return template('blogOne')

@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='./slidesOSINT')

# @route('/blog/<post>')
# def blog(post):

# 	conn = sqlite3.connect('data.db')
# 	c = conn.cursor()
# 	c.execute('SELECT task FROM blog WHERE id IS ?', (post,))
# 	text = c.fetchone()
# 	c.close()

# 	return template('blank', content=text[0])

# new post

# @get('/new')
# def new():
# 	return template('new')

# @post('/new')
# def new():
# 	text = request.forms.get('text')

# 	conn = sqlite3.connect('data.db')
# 	c = conn.cursor()
# 	c.execute('INSERT INTO blog (task, status) VALUES (?, ?)', (text, 1))
# 	conn.commit()
# 	c.close()

# 	return template('blank', content=text)


# need an actual admin panel later

# admin

# @get('/admin')
# def admin():
# 	return template('admin', content='')

# @post('/admin')
# def admin():
# 	text = request.forms.get('text')

# 	conn = sqlite3.connect('data.db')
# 	c = conn.cursor()
# 	c.execute('INSERT INTO adminGuesses (text) VALUES (?)', (text,))
# 	conn.commit()
# 	c.close()

# 	# admin = True
# 	# if admin:
# 	# 	return 'You are an admin! :)'
# 	# else:
# 	# 	return "You're not an admin, you're a goose!"

# 	# return "You have been given the admin power"

# 	return template('admin', content='Unfortunately you entered the wrong admin password. Please try again.')

# admin panel to see all the guesses

# @route('/adminGuesses')
# def adminGuesses():
# 	conn = sqlite3.connect('data.db')
# 	c = conn.cursor()
# 	c.execute('SELECT * FROM adminGuesses;')
# 	guesses = c.fetchall()
# 	c.close()

# 	return template('adminGuesses', guesses=guesses)

# # hacked

# @route('/hacked')
# def hacked():
# 	return template('hacked')

# ctf

# @route('/ctf')
# def ctf():
# 	return template('blank', content='Gentleman, welcome to Fight Club')


# friendship trivia

# @get('/trivia')
# def trivia():
# 	return template('trivia')

# @post('/trivia')
# def trivia():
# 	friend = request.forms.get('friend')
# 	question = request.forms.get('question')

# 	conn = sqlite3.connect('data.db')
# 	c = conn.cursor()
# 	c.execute('INSERT INTO trivia (friend, question) VALUES (?, ?)', (friend, question))
# 	conn.commit()
# 	c.close()

# 	return template('trivia')

# @route('/play')
# def play():
# 	conn = sqlite3.connect('data.db')
# 	c = conn.cursor()
# 	c.execute('SELECT * FROM trivia ORDER BY RANDOM() LIMIT 1')
# 	text = c.fetchone()
# 	c.close()

# 	text = text[1] + ':' + text[2]

# 	return template('blank', content=text)


# Signup System

# @get('/signup')
# def signup():
#     return template('signup')

# @post('/signup')
# def signup():
#     username = request.forms.get('username')
#     password = request.forms.get('password')

#     conn = sqlite3.connect('data.db')
#     c = conn.cursor()
#     c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
#     conn.commit()
#     c.close()

#     return template('blank', content='Thank you for signing up. Please log in.')

# Login System

# @get('/login')
# def login():
#     return template('login')

# @post('/login')
# def login():
#     username = request.forms.get('username')
#     password = request.forms.get('password')

#     conn = sqlite3.connect('data.db')
#     c = conn.cursor()
#     c.execute('SELECT password FROM users WHERE username IS ?', (username,))
#     actual = c.fetchone()
#     c.close()

#     if password == actual[0]:
#         response.set_cookie('cookie', username)
#         return template('blank', content='You have successfully logged in')
#     else:
#         return template('blank', content='Login failed.')

# # Logout System

# @route('/logout')
# def logout():
# 	response.delete_cookie('cookie')
# 	return template('blank', content='You have successfully logged out')

# Miscallaneous files

@route('/style.css')
def style():
	return static_file('/style.css', root='./')

@route('/robots.txt')
def robots():
	return static_file('/robots.txt', root='./')

# @route('/cookie')
# def cookie():
# 	return template('blank', content=request.get_cookie('cookie'))

# Media

# @route('/images/<name>')
# def images(name):
# 	return static_file(name, root='./views/images')

# @route('/videos/<name>')
# def images(name):
# 	return static_file(name, root='./views/videos')


# Functions


# errors

@error(404)
def error404(error):
	return '<h1>404: Page not found</h1>'

@error(405)
def error405(error):
	return '<h1>405: Method not allowed</h1>'

@error(500)
def error500(error):
	return '<h1>500: Internal server error</h1>'


# for dev
run(host='localhost', port=8080, debug=True, reloader=True, server='paste')


#bottle.run(host='0.0.0.0', port=80, server='paste')


# for live
# run(host=?, port=80?)
