#PART ONE
#class MathDojo(object):
#     def __init__(self):
#         self.results = 0
#     def add(self, *args):
#         self.addition = 0
#         for value in args:
#             self.addition += value
#         self.results += self.addition #WHEN WE SUBTRACT WE ADD UP THE VALS AND THEN SUBTRACT FROM RESULT WHICH BEGINS AT 0
#         return self
#     def subtract(self, *args):
#         self.subtraction = 0
#         for value in args:
#             self.subtraction += value
#         self.results -= self.subtraction
#         return self


#md = MathDojo().add(2).add(2,5).add(9,10).subtract(22).results
#print md

#PART TWO
#SUPPORT LISTS AND INTS

#class MathDojo(object):
#     def __init__(self):
#         self.results = 0
#     def add(self, *args):
#         self.addition = 0
#         for x in args:
#            if type(x) == list: #checks if X is a List
#                for val in x:
#                    self.addition += val #adds Value in list (self.addition)
#            elif type(x) == int or float: #checks if X is either INT or FLOAT
#                self.addition += x 
#         self.results += self.addition
#         return self
#     def subtract(self, *args):
#         self.subtraction = 0
#         for x in args:
#            if type(x) == list: #Checks if X is a List
#                 for val in x: #if its a list then we iterare through values
#                     self.subtraction -= val # subtract the value in the List from (self.addition)
#            elif type(x) == int or float: #checks if X is INT or FLOAT
#                self.subtraction -= x
#         self.results += self.subtraction
#         return self
#     def show(self,results):
#        print "The Result is:", self.results
#PART 3
#SUPPORT TUPLES

class MathDojo(object):
     def __init__(self):
         self.results = 0
     def add(self, *args):
         self.addition = 0
         for x in args:
            if type(x) == list: #checks if X is a List
                for val in x:
                    self.addition += val #adds Value in list (self.addition)
            elif type(x) == int or type(x) ==float: #checks if X is either INT or FLOAT
                self.addition += x
            elif type(x) == tuple:
                for val in x:
                    self.addition += val
         self.results += self.addition
         return self
     def subtract(self, *args):
         self.subtraction = 0
         for x in args:
            if type(x) == list: #Checks if X is a List
                 for val in x: #if its a list then we iterare through values
                     self.subtraction -= val # subtract the value in the List from (self.addition)
            elif type(x) == int or type(x) == float: #checks if X is INT or FLOAT
                self.subtraction -= x
            elif type(x) == tuple:
                for val in x:
                    self.subtraction -= val
         self.results += self.subtraction
         return self
     

md = MathDojo()
md.add([1], 3,4,(3,3)).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3], (3))
print md.results




        
