from citoplasma.lists import SimpleList
from bottle import request, redirect 
from citoplasma.urls import add_get_parameters
from citoplasma.templates import set_flash_message
from cromosoma.formsutils import show_form
from citoplasma.i18n import I18n
from cromosoma.formsutils import obtain_post

class GenerateAdminClass:
    
    def __init__(self, model, url, t):
        
        self.model_name=''
        
        self.model=model
        
        self.t=t

        self.list=SimpleList(model, url, t)
        
        self.arr_fields_edit=model.fields.keys()
        
        self.url=url
        
        self.safe=0;
        
        self.arr_links={}
        
        self.hierarchy=None
        
        self.text_add_item=''
        
        self.no_insert=False
        
        self.no_delete=False
        
        self.id=0

    def show(self):
        
        request.query.get('op_admin', '0')
        
        if request.query.op_admin=='1':
            
            if len(self.model.forms)==0:
                self.model.create_forms(self.arr_fields_edit)
            
            if self.id==0:
                post={}
                form=show_form(post, self.model.forms, self.t, False)
                
            return self.t.load_template('utils/insertform.phtml', admin=self, form=form)
        
        elif request.query.op_admin=='2':
            
            post=obtain_post()
            
            if self.model.insert(post):
                set_flash_message(I18n.lang('common', 'task_successful', 'Task successful'))
                redirect(self.url)
            else:
                form=show_form(post, self.model.forms, self.t, True)
                return self.t.load_template('utils/insertform.phtml', admin=self, form=form)
            """
            username = request.forms.get('username', '')
            password = request.forms.get('password', '')
            """
            
            
            
            pass
            
        else:
            return self.t.load_template('utils/admin.phtml', admin=self)
            
