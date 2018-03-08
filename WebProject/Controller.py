'''
Created on Mar 6, 2018

@author: Eric
'''

import web

urls = (
    '/', 'home'
    )
app = web.application(urls, globals())
render = web.template.render("Views/Templates", base = "MainLayout")
#Define Classes/Routes

class home:
    def GET(self):
        return render.Home()
    
if __name__ == '__main__':
    app.run()
    
    