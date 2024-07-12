class Sum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def total_sum(self):
        return self.num1 + self.num2
    
s = Sum(5,10)
print(s.sum())

