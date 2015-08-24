#!/usr/bin/python3

from settings import config

def make_url(module, controller, method, query_args={}):
    
    get_query=''
    
    if len(query_args)>0:
        
        get_query='?'+"&amp;".join( [x+'='+y for x,y in query_args.items()] )
    
    return config.base_url+module+'/'+controller+'/'+method+get_query