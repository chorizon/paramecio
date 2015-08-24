#!/usr/bin/python3

from citoplasma.templates import ptemplate
from citoplasma.urls import make_url

t=ptemplate('welcome')

def home(request, **args):

    return t.load_template('welcome.html', title="Welcome to Paramecio!!!", content="The simple web framework writed in Python3!!!")

def page(request, **args):
    
    return t.load_template('index.html', title="A simple example of a page", id=str(args['id']), value=request.query.value)

def test(request, **args):
    
    return make_url('app', 'page', 'index', {'pepe': 'pepo', 'pepa':'pipa'})

