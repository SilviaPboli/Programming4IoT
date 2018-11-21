import requests

if __name__=='__main__':
    while True:
        operation=input('insert operator -> add sub mult div  :\n')
        op1=input('first operand: ')
        op2=input('second operand: ')
        
        if (operation!='add' and operation!='sub' and operation!='mult' and operation!='div'):
            raise Exception('invalid operation')
            
        r = requests.get('http://localhost:8080/'+operation+'?'+'op1='+op1+'&'+'op2='+op2).json()
        print('operation: %r operands: %r %r result: %r ' %(r['operation'],r['op1'],r['op2'],r['result']))
