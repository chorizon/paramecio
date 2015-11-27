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
            
            post={}
            
            if len(self.model.forms)==0:
                self.model.create_forms(self.arr_fields_edit)
            
            request.query.get('id', '0')
            
            if request.query.id!='0':
                post=self.model.select_a_row(request.query.id)
            
            if post!=None:
            
                form=show_form(post, self.model.forms, self.t, False)
                    
                return self.t.load_template('utils/insertform.phtml', admin=self, form=form, id=request.query.id)
        
        elif request.query.op_admin=='2':
            
            post=obtain_post()
            
            insert_row=self.model.insert
            
            request.query.get('id', '0')
            
            if request.query.id!='0':
                insert_row=self.model.update
                
                self.model.conditions=['WHERE `'+self.model.name+'`.`'+self.model.name_field_id+'`=%s', [request.query.id]]
            
            if insert_row(post):
                set_flash_message(I18n.lang('common', 'task_successful', 'Task successful'))
                redirect(self.url)
            else:
                form=show_form(post, self.model.forms, self.t, True)
                return self.t.load_template('utils/insertform.phtml', admin=self, form=form)

            
            pass
            
        elif request.query.op_admin=='3':
    
            if request.query.id!='0':
                self.model.conditions=['WHERE `'+self.model.name+'`.`'+self.model.name_field_id+'`=%s', [request.query.id]]
                self.model.delete()
                set_flash_message(I18n.lang('common', 'task_successful', 'Task successful'))
                redirect(self.url)
    
        else:
            return self.t.load_template('utils/admin.phtml', admin=self)

