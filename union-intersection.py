class unionSet():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def intersectionValue(self):
        returnTuple = ()
        for item in self.a:
            if item  in self.b:
                returnTuple += (item,)
        return returnTuple
    def unionValues(self):
        returnTuple = ()
        for item in self.a:
            if item not in returnTuple:
                returnTuple +=(item,)
        for item in self.b:
            if item not in returnTuple:
                returnTuple +=(item,)      
        return returnTuple
        
                
a = (1,2,3,4,5,5,6)
b = (1,2,3,7,8)   
unionSet(a,b).intersectionValue()
unionSet(a,b).unionValues()

