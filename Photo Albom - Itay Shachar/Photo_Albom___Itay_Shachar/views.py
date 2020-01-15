"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Photo_Albom___Itay_Shachar import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/PhotoAlbum')
def PhotoAlbum():
    """Renders the contact page."""
    return render_template(
        'PhotoAlbum.html',
        title='Photo Album',
        year=datetime.now().year,
        message='Welcome to my Photo Album which shows the "Top 10 richest people in 2019 around the world ".'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
