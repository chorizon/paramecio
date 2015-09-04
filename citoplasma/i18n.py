#!/usr/bin/python3

from settings import config

def load_lang(**args):
    
    for module in args:
    
        if module in config.modules:
    
            lang_path=config.base_modules+'.'+module+'.i18n'
            
        else:
            lang_path='i18n'

        #gettext.bindtextdomain(module, lang_path)
        
        
        
        #gettext.textdomain(module)
        # _= gettext.gettext
        

class I18n:
    
    l={}
    
    @staticmethod
    def lang(module, symbol, text_default):
        
        I18n.l[module]=I18n.l.get(module, {})
        
        I18n.l[module][symbol]=I18n.l[module].get(symbol, text_default)
        
        return I18n.l[module][symbol]


