#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Python Cheat Sheet: Web Development
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import flask
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

import django
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.contrib import admin

from rest_framework import viewsets, serializers

# 1. Flask Web Framework

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

# Route with variable
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

# HTTP methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    else:
        return show_login_form()

# Rendering templates
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

# Redirects
@app.route('/redirect')
def redirect_example():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

# Tip: Use debug=True during development for auto-reloading and detailed error pages

# Database integration with Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Tip: Use Flask-Migrate for database migrations in Flask

# Form handling with Flask-WTF
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

# User session management with Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    # ... (user model definition)
    pass

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/protected')
@login_required
def protected():
    return f'Hello, {current_user.username}!'

# Tip: Use Flask-Login for handling user sessions and authentication

# RESTful API with Flask-RESTful
from flask_restful import Api, Resource, reqparse

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

# Tip: Use Flask-RESTful for building RESTful APIs quickly

# 2. Django Web Framework

# Create a new Django project
# django-admin startproject myproject

# Create a new Django app
# python manage.py startapp myapp

# settings.py
INSTALLED_APPS = [
    # ...
    'myapp',
]

# models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

# views.py
def home(request):
    return HttpResponse("Hello, World!")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

# urls.py (in myapp)
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
]

# urls.py (in myproject)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

# Tip: Use Django's built-in admin interface for easy management of your models

# Django Forms
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# Django's authentication system
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    # ... (view logic)
    pass

# Tip: Use Django's built-in authentication system for user management

# Django Rest Framework
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'pub_date']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Tip: Use Django Rest Framework for building powerful APIs with minimal code

# 3. Web Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

url = 'http://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements
title = soup.title.string
paragraphs = soup.find_all('p')

for p in paragraphs:
    print(p.text)

# Tip: Always respect robots.txt and website terms of service when scraping

# 4. Asynchronous Web Development with FastAPI

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}

# Tip: FastAPI provides automatic API documentation with Swagger UI

# 5. Web Sockets with Flask-SocketIO

from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    emit('response', {'data': 'Message received'})

if __name__ == '__main__':
    socketio.run(app)

# Tip: Use web sockets for real-time, bi-directional communication between client and server

# 6. Security Considerations

# CSRF protection in Flask
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

# XSS prevention
@app.after_request
def add_security_headers(resp):
    resp.headers['Content-Security-Policy'] = "default-src 'self'"
    return resp

# SQL Injection prevention (using SQLAlchemy)
user = User.query.filter_by(username=username).first()  # Safe
# Don't do this: f"SELECT * FROM users WHERE username = '{username}'"  # Unsafe

# Tip: Always sanitize user inputs and use parameterized queries

# 7. Deployment

# Requirements file
# pip freeze > requirements.txt

# Gunicorn for production server
# gunicorn --workers 3 --bind unix:myapp.sock -m 007 wsgi:app

# Docker for containerization
"""
# Dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
"""

# Tip: Use environment variables for sensitive information in production

# 8. Testing Web Applications

# Flask testing
import unittest

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# Django testing
from django.test import TestCase

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Test Post", content="Test Content")

    def test_post_content(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.content, "Test Content")

# Tip: Write tests for your views, models, and forms to ensure your application works as expected

# 9. API Design Best Practices

# Use meaningful HTTP methods
@app.route('/api/posts', methods=['GET'])
def get_posts():
    # Retrieve posts

@app.route('/api/posts', methods=['POST'])
def create_post():
    # Create a new post

# Use appropriate status codes
from flask import abort

@app.route('/api/post/<int:post_id>')
def get_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        abort(404)  # Not Found
    return jsonify(post.to_dict())

# Versioning
@app.route('/api/v1/posts')
def api_v1_posts():
    # Version 1 of the API

# Tip: Design your API to be RESTful, consistent, and easy to use

# 10. Performance Optimization

# Caching with Flask-Caching
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/expensive-operation')
@cache.cached(timeout=60)  # Cache for 60 seconds
def expensive_operation():
    # ... perform expensive operation
    return result

# Database query optimization
# Use select_related() and prefetch_related() in Django
posts = Post.objects.select_related('author').prefetch_related('comments')

# Tip: Profile your application to identify and optimize bottlenecks

# Best Practices and Tips:

# 1. Follow the principle of "Don't Repeat Yourself" (DRY) in your code.
# 2. Use virtual environments to isolate project dependencies.
# 3. Implement proper error handling and logging in production.
# 4. Use asynchronous programming for I/O-bound operations to improve performance.
# 5. Implement rate limiting for APIs to prevent abuse.
# 6. Use HTTPS in production to encrypt data in transit.
# 7. Regularly update your dependencies to patch security vulnerabilities.
# 8. Implement proper user authentication and authorization.
# 9. Use database indexes to optimize query performance.
# 10. Implement proper error handling and provide meaningful error messages.
# 11. Use content delivery networks (CDNs) for serving static files.
# 12. Implement database migrations for managing schema changes.
# 13. Use task queues (like Celery) for handling long-running tasks asynchronously.
# 14. Implement proper logging for debugging and monitoring in production.
# 15. Use configuration management to handle different environments (development, staging, production).

# This concludes the enhanced detailed Python Cheat Sheet for Web Development