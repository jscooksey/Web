from flask import render_template, flash, redirect, url_for, current_app
from . import articles
from .. import db

@articles.route('/')
def index():
    return render_template('index.html', title='Overview')

@articles.route('/about')
def about():
    return render_template('about.html', title='About')

