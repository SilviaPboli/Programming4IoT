
class calculator:
    def add(self, a,b):
        result = a+b
        #print("the result is : %d" % result)
        return (result)

    def sub(self, a, b):
        result = a-b
        #print("the result is : %d" % result)
        return (result)

    def div(self, a,b):
        if(a == 0 or b == 0):
            print("error, put other values: ")
            exit(1)
        else:
            result = a/b
        #print("the result is : %d" % result)
        return (result)


    def mult(self, a,b):
        result = a*b
        #print("the result is : %d" % result)
        return (result)


