#!/usr/bin/python3

urls={}

urls['']=[['get', '', 'welcome.index.home']]

urls['/page']=[['get', '/<id:int>', 'welcome.index.page']]

urls['/test']=[['get', '', 'welcome.index.test'], ['get', '/<id:int>', 'welcome.index.test']]

urls['/ajax/home']=[['get', '', 'welcome.ajax.index.home']]

#rewrite={'/page/<id:int>': 'app.index.page'}
