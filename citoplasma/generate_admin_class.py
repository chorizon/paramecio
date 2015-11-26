from citoplasma.lists import SimpleList
from citoplasma.sessions import get_session
from citoplasma.urls import add_get_parameters

class GenerateAdminClass:
    
    def __init__(model, url, t):
        self.model_name=''

        self.list=SimpleList(model, url, t)
        
        #For the future
        
        self.arr_fields_insert={}
        
        self.arr_fields_edit={}
        
        self.url=url
        
        self.safe=0;
        
        self.arr_links={}
        
        self.hierarchy
        
        self.text_add_item=''
        
        self.no_insert=0
        
        self.no_delete=0


    def show():
        pass