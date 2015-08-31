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
            
            path_module=config.base_modules+'/'+module+'/media/'
            
            file_path_module=path_module+filename
            
            path=config.base_modules+'/'+module+'/media/'
            
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

@route("/")
#@route("/<module>")
#@route("/<module>/<controller>")

def index(**args):
    
    global module_loaded
    
    """
    
    
    if not "controller" in args:
        args["controller"]="index"
    
    arr_func=request['bottle.route'].rule.split('/')
    
    #arr_func.remove(0)
    
    num_args=len(arr_func)
    
    extra_dir=''
    
    if num_args>=4:
        
        args["func"]=arr_func[3]+extra_dir
    else:
        args["func"]="home"
    
    
    if not "func" in args:
        args["func"]="home"
    """
    """
    print(request['bottle.route'].rule)
    
    if not "module" in args:
        args["module"]=config.default_module
        
    if not "controller" in args:
        args["controller"]="index"
        
    if not "func" in args:
        args["func"]="home"
    """
    
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
    
    """
    if not args["module"] in config.modules:
        abort(404, "Page not found")
    """
    
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
    # Cleaning args of module, controller and func
    
    """"
    del args['module'];
    del args['controller'];
    del args['func'];
    """
    
    return func(request, **args)

#Import config urls 

for module in config.modules:
    
    try:
        
        urls=import_module(config.base_modules+'.'+module+'.urls')
        
        for method, turl in urls.urls.items():
            
            for url in turl:
                
                final_route="/"+module+method+url[1]
                
                func_route=getattr(sys.modules[__name__], url[0]);
                
                index=func_route(final_route)(index)       
                
                #Add routes to dictionary routes
               
                routes[final_route]=config.base_modules+'.'+url[2]
                
                add_func_static_module(module)

    except:
        
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)

app = default_app()

if config.session_activated==True:
    #Create dir for sessions
    
    if not os.path.isdir(config.session_opts['session.data_dir']):
        os.makedirs(config.session_opts['session.data_dir'], 0o700, True)
    
    app = SessionMiddleware(app, config.session_opts)

if __name__ == "__main__":
    run(app=app, host=config.host, server=config.server_used, port=config.port, debug=config.debug, reloader=config.reloader)


