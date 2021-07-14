from flask import render_template

def get_page(name, context={}):
    path = get_page_path(name)
    return render_template(path, **context)

def get_page_path(name, context={}):
    return f"pages/{name}.html"

def get_layout_path(name):
    return f"layouts/{name}.html"