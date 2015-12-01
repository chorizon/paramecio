#!/usr/bin/python3

from citoplasma.templates import ptemplate
from modules.admin.models.admin import UserAdmin
from citoplasma.i18n import load_lang, I18n
from citoplasma.urls import make_url, add_get_parameters
from citoplasma.sessions import get_session
from bottle import get,post
from settings import config
from citoplasma.lists import SimpleList
from citoplasma.generate_admin_class import GenerateAdminClass
from citoplasma.httputils import GetPostFiles
from cromosoma.formsutils import show_form
from cromosoma.coreforms import PasswordForm
#from citoplasma.login import LoginClass
# Check login

t=ptemplate('admin')

load_lang('admin', 'common')
@get('/'+config.admin_folder)
@get('/'+config.admin_folder+'/<module>')
@post('/'+config.admin_folder+'/<module>')
def home(module=''):
    """
    s=args['session']
    #print(s['test'])
    s['test'] = s.get('test', 0)+1
    
    print(s['test'])
    
    #del s['test']
    
    #s.save()
    
    s['test'] = 'pepe'
    s.save()
    """
    
    """
    s = request.environ.get('paramecio.session')
    s['test'] = 'pepe' #s.get('test',0) + 1
    s.save()
    """
    #return 'Test counter: %d' % s['test']
    
    #user_admin.insert({'username': 'pepe', 'password': 'pitorro', 'token_recovery': 'vaamoos'}, False)
    
    #Load modules and submodules and make menu
    #Pass environment to login class
    """
    s = request.environ.get('beaker.session')
    
    if 'login' not in s:
        return t.load_template('admin/content.html', title="Welcome to "+args['module'], content='No logueado')"""
    """
    list_user=SimpleList(user_admin, '', t)
    
    list_user.url=make_url('admin/welcome', {})
    
    list_user.fields_showed=['username', 'password']
    
    list_user.search_fields=['username']
    """
    #list_user.fields=['id']
    
    #list_user.set_fields_no_showed(['id'])
    
    #list_user.begin_page=request.query.begin_page
    """
    url=make_url('admin/welcome', {})
    
    admin=GenerateAdminClass(user_admin, url, t)
    
    #admin.list=SimpleList(user_admin, '', t)
    
    admin.list.fields_showed=['username', 'password']
    
    admin.list.search_fields=['username']
    
    admin.list.limit_pages=5
    """
    
    #check if login
    
    user_admin=UserAdmin()
    
    s=get_session()
    
    if 'login' in s:
        
        if s['privileges']==2:
    
            if module in config.modules:
                
                #Load module
                
                return t.load_template('admin/content.html', title=I18n.lang('admin', 'admin_module', "Admin ")+module, content="")
                
            else:
                return t.load_template('admin/index.html', title=I18n.lang('admin', 'welcome_to_paramecio', "Welcome to Paramecio Admin!!!"))
    else:
        
        user_admin.conditions=['WHERE privileges=%s', 2]
        
        c=user_admin.select_count()
        
        if c>0:
        
            post={}

            user_admin.fields['password'].required=True

            user_admin.create_forms(['username', 'password'])
            
            forms=show_form(post, user_admin.forms, t, yes_error=False)

            return t.load_template('admin/login.phtml', forms=forms)
        else:
        
            post={}
            
            set_extra_forms_user(user_admin)
            
            forms=show_form(post, user_admin.forms, t, yes_error=False)

            return t.load_template('admin/register.phtml', forms=forms)
    
@post('/'+config.admin_folder+'/login')
def login():
    
    post=GetPostFiles.obtain_post()
    

@post('/'+config.admin_folder+'/register')
def register():
    
    user_admin=UserAdmin()
    
    GetPostFiles.obtain_post()
    
    set_extra_forms_user(user_admin)
    
    GetPostFiles.post.append('privileges', 2)
    
    if user_admin.insert(GetPostFiles.post, False):
    
        error= {'error': 0}
        
    else:       
        
        error= {'error': 1}
        
        for field in user_admin.fields.values():
            
            error[field.name]=field.txt_error
        
        error['global']=user_admin.query_error
        
    #user_admin.fields['password'].protected=True
    
    return error
    
    pass

def set_extra_forms_user(user_admin):
    
    user_admin.fields['password'].required=True
    user_admin.fields['email'].required=True

    user_admin.create_forms(['username', 'email', 'password'])
    
    user_admin.forms['repeat_password']=PasswordForm('repeat_password', '')
    
    user_admin.forms['repeat_password'].required=1
    
    user_admin.forms['repeat_password'].label=I18n.lang('common', 'repeat_password', 'Repeat Password')


    """user_admin.create_forms()
    
    users=user_admin.select()"""

#By default id is not showed