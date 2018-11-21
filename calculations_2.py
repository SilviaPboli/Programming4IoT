
class calculator:
    def add(self, num_list):
        result = num_list[0]
        for i in range(1,len(num_list)):
            result += num_list[i]
        #print("the result is : %d" % result)
        return (result)

    def sub(self, num_list):
        result = num_list[0]
        for i in range(1,len(num_list)):
            result =   result - num_list[i]
        #print("the result is : %d" % result)
        return (result)

    def div(self, num_list):
        result = num_list[0]
        for i in range(1,len(num_list)):
            result = result / num_list[i]
        #print("the result is : %d" % result)
        return (result)


    def mult(self, num_list):
        result = num_list[0]
        for i in range(1,len(num_list)):
            result = result * num_list[i]
        #print("the result is : %d" % result)
        return (result)


