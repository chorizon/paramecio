import os, sys, traceback
from importlib import import_module
from bottle import route, get, post, run, default_app, abort, request, static_file
from settings import config

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

@route("/")
@route("/<module>")
@route("/<module>/<controller>")
def index(**args):
    
    if not "module" in args:
        args["module"]=config.default_module
    
    if not "controller" in args:
        args["controller"]="index"
    
    arr_func=request['bottle.route'].rule.split('/',maxsplit=4)
    
    if len(arr_func)>=4:
        args["func"]=arr_func[3]
    else:
        args["func"]="home"
    
    """
    if not "func" in args:
        args["func"]="home"
    """
    
    #Import function from module
    
    if not args["module"] in config.modules:
        abort(404, "Page not found")
    
    try:
    
        module=import_module(config.base_modules+'.'+args["module"]+'.'+args["controller"])
    
    except:
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)
        abort(404, "Page not found")
    
    func=getattr(module, args["func"])
    
    # Cleaning args of module, controller and func
    
    del args['module'];
    del args['controller'];
    del args['func'];
    
    return func(request, **args)

#Import config urls 

for module in config.modules:
    
    try:
        
        urls=import_module(config.base_modules+'.'+module+'.urls')
        
        for module, turl in urls.urls.items():
            
            for url in turl:
            
                final_route="/<module>/<controller>/"+module+url[1]
                
                func_route=getattr(sys.modules[__name__], url[0]);
                
                index=func_route(final_route)(index)       
                
                add_func_static_module(module)

    except:
        
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)

if __name__ == "__main__":
    run(host=config.host, server=config.server_used, port=8080, debug=True, reloader=True)

app = default_app()


