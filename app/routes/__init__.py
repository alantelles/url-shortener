import traceback
from flask import render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound

import app.helpers.templates as tp
import app.services.shortener as shortener
from app import app

@app.route('/', methods=["GET"])
def index():
    context = {'base_template': tp.get_layout_path('base')}
    return tp.get_page('index', context)

@app.route('/check', methods=["GET"])
def new_short_url():
    context = {
        'base_template': tp.get_layout_path('base')
    }
    url = request.args.get('short')
    if url:
        context['short'] = url
        valid_url =  shortener.check_short_url(url)
        if valid_url:
            context['destination'] = valid_url
            return tp.get_page('result', context)

        return tp.get_page('url_not_found', context)
    context['header'] = "Requisição inválida"
    context['message'] = "Não foi enviada uma URL para validação"
    context['code'] = 400
    return tp.get_page('error', context)
    

@app.route('/new', methods=["POST"])
def save_short_url():
    url = request.form.get('complete_url')
    short_url = shortener.save_new_url(url)

    if short_url:
        return redirect(url_for('new_short_url', short=short_url))

@app.route('/errors/<err_type>', default={'err_type': 'error'}, methods=["GET"])
def show_error_page(err_type):
    context = {'base_template': tp.get_layout_path('base')}
    if err_type == 'not_found':
        context['header'] = 'URL encurtada não existe'
        context['message'] = 'A URL encurtada dada não está nos nossos registros'
        context['code'] = 404

    elif err_type == 'page_not_found':
        context['header'] = "Página não encontrada",
        context['message'] = "A página requisitada não existe neste site",
        context['code'] = 404

    else:
        context['header'] = "Erro!",
        context['message'] = "Algum erro ocorreu. Estamos trabalhando na solução do problema",
        context['code'] = 500

    
    return tp.get_page('error', context)

@app.errorhandler(NotFound)
def handle_not_found_exception(e):
    context = {
        'base_template': tp.get_layout_path('base'),
        'header': "Página não encontrada",
        'message': "A página requisitada não existe neste site",
        'code': 404
    }
    return tp.get_page('error', context)

@app.errorhandler(Exception)
def handle_not_found_exception(e):
    traceback.print_exc()
    context = {
        'base_template': tp.get_layout_path('base'),
        'header': "Erro!",
        'message': "Algum erro ocorreu. Estamos trabalhando para corrigir o problema.",
        'code': 500
    }
    return tp.get_page('error', context)