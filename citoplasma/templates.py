#!/usr/bin/python

from jinja2 import Template, Environment, FileSystemLoader
from citoplasma.urls import make_url, make_media_url, make_media_url_module, add_get_parameters
from settings import config

# Preparing envs for views of modules, and views of 

""" A simple function for load views from themes using jinja2 

Env use loader = FileSystemLoader(['/path/to/templates', '/other/path'])
env = Environment(loader=FileSystemLoader(['/path/to/templates', '/other/path']))
template = env.get_template('mytemplate.html')
"""

class ptemplate:
    
    autoescape_ext=('html', 'htm', 'xml')
    
    def __init__(self, module):
        
        self.env=self.env_theme(module)
        
        #Adding basic filters for urls
        
        self.add_filter(make_url)
        
        self.add_filter(make_media_url)
        
        self.add_filter(make_media_url_module)
        
        self.add_filter(add_get_parameters)
    
    def guess_autoescape(self, template_name):
        
        if template_name is None or '.' not in template_name:
            return False
        
        ext = template_name.rsplit('.', 1)[1]
        return ext in self.autoescape_ext

    def env_theme(self, module):

        theme_templates='themes/'+config.theme+'/templates'

        module_templates=config.base_modules+'/'+module+'/templates'

        return Environment(autoescape=self.guess_autoescape, loader=FileSystemLoader([theme_templates, module_templates]))

    def load_template(self, template_file, **arguments):
        
        template = self.env.get_template(template_file)
        
        return template.render(arguments)

    def add_filter(self, filter_name):

        self.env.filters[filter_name.__name__]=filter_name

