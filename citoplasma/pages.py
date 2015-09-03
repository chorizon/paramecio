#!/usr/bin/python3

from math import ceil, floor
from citoplasma.urls import add_get_parameters
#from citoplasma.i18n import lang
import gettext
gettext.bindtextdomain('common', 'i18n')
gettext.textdomain('common')
_ = gettext.gettext

class Pages: 

    css_class='link_pages'

    @staticmethod
    def show( begin_page, total_elements, num_elements, link ,initial_num_pages=20, variable='begin_page', label='', func_jscript=''):

        pages='';

        if begin_page>total_elements:
            begin_page=0

        # Calculamos el total de todas las páginas

        total_page=ceil(total_elements/num_elements)
        
        # Calculamos en que página nos encontramos

        actual_page=ceil(begin_page/num_elements)

        # Calculamos el total de intervalos

        total_interval=ceil(total_page/initial_num_pages)

        # Calculamos el intervalo en el que estamos

        actual_interval=floor(actual_page/initial_num_pages)

        # Calculamos el elemento de inicio del intervalo

        initial_page=ceil(actual_interval*initial_num_pages*num_elements)

        last_page=ceil(actual_interval*initial_num_pages*num_elements)+ceil(initial_num_pages*num_elements)

        if last_page>total_elements:
            last_page=total_elements

        if initial_page>0:
            initial_link=add_get_parameters(link, {variable: 0});
            middle_link=add_get_parameters(link, {variable: (initial_page-num_elements).label} );
            pages += "<a class=\""+self.css_class+"\" href=\"initial_link\" onclick=\"func_jscript\">1</a> <a class=\""+self.css_class+"\" href=\"middle_link\">&lt;&lt;</a> "

        arr_pages={}

        #for(x=initial_page;x<last_page;x+=num_elements)
        for x in range(initial_page, last_page):
            
            middle_link=add_get_parameters(link, {variable: x.label} )

            num_page=ceil(x/num_elements)+1;
            arr_pages[x]="<a class=\""+self.css_class+"\" href=\"middle_link\" onclick=\"func_jscript\">num_page</a> "
            arr_pages[begin_page]='<span class="selected_page">'+num_page+'</span> ';
            pages += arr_pages[x]
            
            x+=num_elements

        
        if last_page<total_elements:

            middle_link=add_get_parameters(link, {variable: x.label} );
            last_link=add_get_parameters(link, {variable: ( ( total_page*num_elements ) - num_elements) } )

            pages += "<a class=\""+self.css_class+"\" href=\"middle_link\" onclick=\"func_jscript\">&gt;&gt;</a> <a class=\"link_pages\" href=\"last_link\" onclick=\"func_jscript\">"+_('common', 'last', 'Last')+"</a>"

        
        return pages


