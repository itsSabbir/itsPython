# Network Programming - Creating web servers with Flask or Django basics - in the Python Programming Language
# ======================================================================================================

# Table of Contents:
# 1. Overview and Historical Context
# 2. Syntax, Key Concepts, and Code Examples
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# 4. Integration and Real-World Applications
# 5. Advanced Concepts and Emerging Trends
# 6. FAQs and Troubleshooting
# 7. Recommended Tools, Libraries, and Resources
# 8. Performance Analysis and Optimization
# 9. How to Contribute

# Author: Sabbir Hossain

import flask
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.urls import path
from django.core.wsgi import get_wsgi_application
from django.db import models
import time
import asyncio
import aiohttp
import unittest
from werkzeug.middleware.profiler import ProfilerMiddleware

# 1. Overview and Historical Context
# ----------------------------------
# Flask and Django are two popular Python web frameworks used for creating web servers
# and applications. They provide tools and libraries to handle HTTP requests, render
# templates, interact with databases, and manage user sessions.

# Historical context:
# - Django was first released in 2005, created by Adrian Holovaty and Simon Willison.
# - Flask was created by Armin Ronacher and first released in 2010.
# - Both frameworks have evolved significantly since their initial releases, with
#   Django focusing on a "batteries-included" approach and Flask emphasizing simplicity
#   and extensibility.

# Significance:
# - Web frameworks simplify the process of building web applications by providing
#   structured ways to handle common web development tasks.
# - They promote code organization, reusability, and separation of concerns.
# - Flask and Django cater to different project sizes and complexity levels, giving
#   developers options based on their specific needs.

# Common use cases:
# - Building RESTful APIs
# - Creating dynamic websites
# - Developing full-stack web applications
# - Prototyping and rapid application development

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Flask Example
def flask_example():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/api/data', methods=['GET'])
    def get_data():
        data = {'message': 'This is some data'}
        return jsonify(data)

    @app.route('/api/echo', methods=['POST'])
    def echo():
        data = request.json
        return jsonify(data)

    if __name__ == '__main__':
        app.run(debug=True)

# Django Example
def django_example():
    # settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'myapp',
    ]

    # models.py
    class Item(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()

    # views.py
    def hello_world(request):
        return HttpResponse("Hello, World!")

    class DataView(View):
        def get(self, request):
            data = {'message': 'This is some data'}
            return JsonResponse(data)

    # urls.py
    urlpatterns = [
        path('', hello_world),
        path('api/data', DataView.as_view()),
    ]

    # wsgi.py
    application = get_wsgi_application()

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

def best_practices():
    # Flask best practices
    app = Flask(__name__)
    
    # Use blueprints for modular applications
    admin = flask.Blueprint('admin', __name__, url_prefix='/admin')
    
    @admin.route('/')
    def admin_index():
        return 'Admin Index'
    
    app.register_blueprint(admin)
    
    # Use application factories
    def create_app(config_filename):
        app = Flask(__name__)
        app.config.from_pyfile(config_filename)
        
        # Initialize extensions
        db.init_app(app)
        
        return app

    # Django best practices
    # Use class-based views
    class ItemListView(View):
        def get(self, request):
            items = Item.objects.all()
            return JsonResponse(list(items.values()), safe=False)

    # Use Django REST framework for APIs
    from rest_framework import viewsets
    from .serializers import ItemSerializer

    class ItemViewSet(viewsets.ModelViewSet):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer

def common_pitfalls():
    # Flask pitfalls
    app = Flask(__name__)
    
    # Pitfall: Using global variables in multi-threaded environments
    counter = 0
    
    @app.route('/increment')
    def increment():
        global counter
        counter += 1  # This is not thread-safe
        return str(counter)

    # Django pitfalls
    # Pitfall: N+1 query problem
    def inefficient_view(request):
        items = Item.objects.all()
        for item in items:
            print(item.related_model.name)  # This will cause N+1 queries

    # Solution: Use select_related or prefetch_related
    def efficient_view(request):
        items = Item.objects.select_related('related_model').all()
        for item in items:
            print(item.related_model.name)  # This will use only 1 query

def advanced_tips():
    # Flask: Custom middleware
    class CustomMiddleware:
        def __init__(self, app):
            self.app = app

        def __call__(self, environ, start_response):
            # Do something before the request
            response = self.app(environ, start_response)
            # Do something after the request
            return response

    app.wsgi_app = CustomMiddleware(app.wsgi_app)

    # Django: Custom middleware
    class CustomMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            # Do something before the view
            response = self.get_response(request)
            # Do something after the view
            return response

# 4. Integration and Real-World Applications
# ------------------------------------------

def flask_restful_api():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.json
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'id': new_user.id, 'username': new_user.username, 'email': new_user.email}), 201

    if __name__ == '__main__':
        db.create_all()
        app.run(debug=True)

def django_rest_framework_api():
    # models.py
    class User(models.Model):
        username = models.CharField(max_length=80, unique=True)
        email = models.EmailField(unique=True)

    # serializers.py
    from rest_framework import serializers

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'username', 'email']

    # views.py
    from rest_framework import viewsets

    class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer

    # urls.py
    from rest_framework.routers import DefaultRouter

    router = DefaultRouter()
    router.register(r'users', UserViewSet)

    urlpatterns = [
        path('api/', include(router.urls)),
    ]

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

async def flask_async_view():
    async def fetch_data(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    urls = [
        'https://api.example.com/data1',
        'https://api.example.com/data2',
        'https://api.example.com/data3'
    ]

    results = await asyncio.gather(*[fetch_data(url) for url in urls])
    return jsonify(results)

# Django Channels for WebSocket support
# channels/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=f"Echo: {text_data}")

# 6. FAQs and Troubleshooting
# ---------------------------

def flask_faq():
    # Q: How to handle CORS in Flask?
    from flask_cors import CORS
    app = Flask(__name__)
    CORS(app)

    # Q: How to use Flask with uWSGI?
    # uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app

def django_faq():
    # Q: How to handle CORS in Django?
    # settings.py
    INSTALLED_APPS = [
        # ...
        'corsheaders',
    ]

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        # ...
    ]

    CORS_ALLOW_ALL_ORIGINS = True

    # Q: How to use Django with Gunicorn?
    # gunicorn myproject.wsgi:application

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------
# Tools and Libraries:
# - Flask-RESTful: For building REST APIs with Flask
# - Django REST framework: For building REST APIs with Django
# - Celery: For background task processing
# - SQLAlchemy: ORM for Flask (and other Python applications)
# - Alembic: Database migration tool for SQLAlchemy
# - Django ORM: Built-in ORM for Django
# - pytest: Testing framework for Python

# Resources:
# - Flask documentation: https://flask.palletsprojects.com/
# - Django documentation: https://docs.djangoproject.com/
# - "Flask Web Development" by Miguel Grinberg
# - "Django for Professionals" by William S. Vincent
# - "Two Scoops of Django" by Daniel Roy Greenfeld and Audrey Roy Greenfeld

# 8. Performance Analysis and Optimization
# ----------------------------------------

def flask_profiling():
    app = Flask(__name__)
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

    @app.route('/profile')
    def profile():
        return 'This route is being profiled'

def django_profiling():
    # settings.py
    MIDDLEWARE = [
        # ...
        'django.middleware.profiling.ProfileMiddleware',
    ]

    # Add ?prof to the URL to enable profiling for that request

def optimize_database_queries():
    # Flask with SQLAlchemy
    users = User.query.options(db.joinedload('posts')).all()

    # Django
    users = User.objects.prefetch_related('posts').all()

# 9. How to Contribute
# --------------------
# To contribute to this note sheet:
# 1. Fork the repository containing this file.
# 2. Make your changes or additions.
# 3. Ensure all code examples are correct and follow the established style.
# 4. Add comments explaining new concepts or functions.
# 5. Update the Table of Contents if necessary.
# 6. Submit a pull request with a clear description of your changes.

# Guidelines for contributions:
# - Maintain the current format and style.
# - Provide working code examples for new concepts.
# - Include performance considerations for new functions.
# - Add relevant references or citations for advanced topics.

def main():
    print("Flask Example:")
    flask_example()

    print("\nDjango Example:")
    django_example()

    print("\nBest Practices:")
    best_practices()

    print("\nCommon Pitfalls:")
    common_pitfalls()

    print("\nAdvanced Tips:")
    advanced_tips()

    print("\nFlask RESTful API Example:")
    flask_restful_api()

    print("\nDjango REST Framework API Example:")
    django_rest_framework_api()

    print("\nFlask Profiling Example:")
    flask_profiling()

    print("\nDjango Profiling Example:")
    django_profiling()

    print("\nOptimize Database Queries Example:")
    optimize_database_queries()

if __name__ == "__main__":
    main()