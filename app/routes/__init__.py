from flask import render_template, request, redirect, url_for, flash

import app.helpers.templates as tp
import app.services.shortener as shortener
from app import app


@app.route('/', methods=["GET"])
def index():
    context = {'base_template': tp.get_layout_path('base')}
    return tp.get_page('index', context)

@app.route('/new', methods=["GET"])
def new_short_url():
    context = {'base_template': tp.get_layout_path('base')}
    url = request.args.get('short')
    if url:
        valid_url =  shortener.check_short_url(url)
        if valid_url:
            return tp.get_page('result', context)

        return tp.get_page('url_not_found', context)
    

@app.route('/new', methods=["POST"])
def save_short_url():
    
    short_url = shortener.create_short_url()
    return redirect(url_for('new_short_url', short=short_url))