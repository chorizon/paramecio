#!/usr/bin/python3

from modules.admin.models.admin import UserAdmin
from citoplasma.urls import make_url
from citoplasma.generate_admin_class import GenerateAdminClass

def admin(t):
    
    user_admin=UserAdmin()
    
    url=make_url('admin/ausers', {})
    
    admin=GenerateAdminClass(user_admin, url, t)
    
    #admin.list=SimpleList(user_admin, '', t)
    
    admin.list.fields_showed=['username', 'password']
    
    admin.list.search_fields=['username']
    
    admin.list.limit_pages=5
    
    return admin.show()