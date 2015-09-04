import os, sys, traceback
from importlib import import_module, reload
from bottle import route, get, post, run, default_app, abort, request, static_file
from settings import config
from beaker.middleware import SessionMiddleware

#Prepare links for static.
#WARNING: only use this feature in development, not in production.

if config.yes_static==True:
    
    @route('/media/<filename:path>')
    def send_static(filename):
        return static_file(filename, root='themes/'+config.theme+'/media/')
    
    def add_func_static_module(module):
        
        @route('/mediafrom/<module>/<filename:path>')
        def send_static_module(module, filename):
            
            path_module=config.base_modules.replace('.', '/')+'/'+module+'/media/'
            
            file_path_module=path_module+filename
            
            path=config.base_modules.replace('.', '/')+'/'+module+'/media/'
            
            file_path=path+filename
            
            if os.path.isfile(file_path):
                return static_file(filename, root=path)
                
            else:
                return static_file(filename, root=path_module)
else:
    
    def add_func_static_module(module):
        pass

routes={}

module_loaded=None
"""
@route("/")
def index():
""" 
"""
    global module_loaded
    
    page_loader=''
    method_loader=''
    rule=request['bottle.route'].rule
    
    if rule=="/":
        page_loader=config.base_modules+'.'+config.default_module+'.index'
        method_loader='home'
    elif rule in routes.keys():
        method_loader=os.path.basename(routes[rule].replace('.', '/'))
        page_loader=routes[rule].replace('.'+method_loader, '')
        
    
    #Import function from module
    
    try:
        
        if config.reloader==True:
            
            if module_loaded==None:
                
                module_loaded=import_module(page_loader)
            else:
                
                reload(module_loaded)
                
        else:
    
            module_loaded=import_module(page_loader)
    
    except:
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)
        abort(404, "Page not found")
    
    try:
    
        func=getattr(module_loaded, method_loader)
        
    except:
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)
        abort(404, "Page not found")
    
    args['session']=load_session()"""
    
    #return "Esto es el index"

#Import config urls 

for module in config.modules:
    
    try:
        
        dir_controllers=os.listdir(config.base_modules.replace('.', '/')+'/'+module)
        
        #arr_views=[x for x in dir_modules if x.find('.py')!=-1 and x.find('__init__')==-1]
        
        for controller in dir_controllers:
            if controller.find('.py')!=-1 and controller.find('__init__')==-1:
                controller=controller.replace('.py', '')
                controllers=import_module(config.base_modules+'.'+module+'.'+controller)
        #print(arr_views)
        
        add_func_static_module(module)
        
        #urls=import_module(config.base_modules+'.'+module+'.urls')
        
        """
        for method, turl in urls.urls.items():
            
            for url in turl:
                
                final_route="/"+module+method+url[1]
                
                func_route=getattr(sys.modules[__name__], url[0]);
                
                index=func_route(final_route)(index)       
                
                #Add routes to dictionary routes
               
                routes[final_route]=config.base_modules+'.'+url[2]
                
                add_func_static_module(module)
        """
    except:
        
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)

app = default_app()

if config.session_enabled==True:
    #Create dir for sessions
    
    if not os.path.isdir(config.session_opts['session.data_dir']):
        os.makedirs(config.session_opts['session.data_dir'], 0o700, True)

    app = SessionMiddleware(app, config.session_opts, environ_key=config.cookie_name)
    
    def load_session():
        return request.environ.get(config.cookie_name)
else:
    def load_session():
        return None

if __name__ == "__main__":
    run(app=app, host=config.host, server=config.server_used, port=config.port, debug=config.debug, reloader=config.reloader)


