class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def dsum(self):  
        return self.a + self.b
    
obj = Sum(10,15)
print(obj.dsum())