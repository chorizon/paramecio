#!/usr/bin/python3

from settings import config

#Simple method for make urls

def make_url(module, controller, method, query_args={}):
    
    """
        This is a method for create urls for the system
        
       
        Keyword arguments:
        module -- The module where search code to execute
        controller -- The controller where search code to execute
        method -- The method to execute
        query_args -- a ser of get variables for add to url
        
    """
    
    get_query=''
    
    if len(query_args)>0:
        
        get_query='?'+"&amp;".join( [x+'='+y for x,y in query_args.items()] )
    
    return config.base_url+module+'/'+controller+'/'+method+get_query

if config.yes_static==True:
    
    def make_media_url(file_path):
        
        return '/media/'+file_path
        
    def make_media_url_module(file_path, module):
        
        return '/mediafrom/'+module+'/'+file_path
else:
    
    def make_media_url(file_path):

        return config.media_url+'media/'+file_path
    
    def make_media_url_module(file_path, module):

        return config.media_url+'media/'+module+'/'+file_path