import cherrypy
import json
from calculations_2 import *

# Exercise_1 follow-up: redesign RESTful-style calculator for exposing full URL
# fashion web services where parameters must be provided slash-separated.
# Example:
# http://localhost:8080/add/10/12/
# se non metti il ? non stai mettendo params--> usi solo uri

oper = calculator()  # object created

class StringGeneratorWebService(object):
    exposed = True
# http://localhost:8080/add?op1=10&op2=12
    def PUT(self, *uri):
        body=cherrypy.request.body.read()
        mydic={}
        mydic=json.loads(body) # body is a json string in postman -> mydic is a python dictionary containing the info od the string

        if (mydic['command'] == 'add'):
            result = oper.add(mydic['operands'])
        elif(mydic['command'] == 'sub'):
            result = oper.sub(mydic['operands'])
        elif(mydic['command'] == 'div'):
            result = oper.div(mydic['operands'])
        elif (mydic['command'] == 'mult'):
            result = oper.mult(mydic['operands'])

        obj1 = {"comand": mydic['command'], "operands": mydic['operands'], "result": result}
        # never change an integer in a string!
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