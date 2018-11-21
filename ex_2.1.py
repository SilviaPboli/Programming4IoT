import cherrypy
import json
import calculations_1

oper = calculations_1.calculator()

class StringGeneratorWebService(object):
    exposed = True
# http://localhost:8080/add?op1=10&op2=12
    def GET(self, *uri, **params):
        x = float(params['op1'])
        y = float(params['op2'])
        result = 0
        print(uri[0])
        if(len(params) > 2 or len(params) <2 ):
            raise Exception ('Wrong Params')
        if (uri[0] == 'add'):
            result = oper.add(x,y)
        elif(uri[0] == 'sub'):
            result = oper.sub(x,y)
        elif(uri[0] == 'div'):
            result = oper.div(x, y)
        elif (uri[0] == 'mult'):
            result = oper.mult(x, y)

        obj1 = {"operation": uri[0], "op1": float(params['op1']), "op2": float(params['op2']), "result": float(result)}
        # now i will make obj1 a json string
        string1 = json.dumps(obj1)

        return string1

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
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