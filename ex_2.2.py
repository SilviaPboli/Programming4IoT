import cherrypy
import random
import string
import json
from calculations_1 import *

# Exercise_1 follow-up: redesign RESTful-style calculator for exposing full URL
# fashion web services where parameters must be provided slash-separated.
# Example:
# http://localhost:8080/add/10/12/
# se non metti il ? non stai mettendo params--> usi solo uri

oper = calculator()  # object created

class StringGeneratorWebService(object):
    exposed = True
# http://localhost:8080/add?op1=10&op2=12
    def GET(self, *uri):
        x = float(uri[1])
        y = float(uri[2])
        result = 0
        print(uri[0])
        if(len(uri) !=3 ):
            raise Exception ('Wrong Params')
        if (uri[0] == 'add'):
            result = oper.add(x,y)
        elif(uri[0] == 'sub'):
            result = oper.sub(x,y)
        elif(uri[0] == 'div'):
            result = oper.div(x, y)
        elif (uri[0] == 'mult'):
            result = oper.mult(x, y)

        obj1 = {"operation": uri[0], "x": uri[1], "y": uri[2], "result": str(result)}
        # now i will make obj1 a json string
        string1 = json.dumps(obj1)

        return string1

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8080})
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            #'tools.session.on': True,
            }
        }
    cherrypy.tree.mount(StringGeneratorWebService(),'/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()