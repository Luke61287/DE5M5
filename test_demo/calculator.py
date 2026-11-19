class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        self.luke = 2.45

    def get_sum(self):
        return self.a + self.b

    def get_subtract(self):
        return self.a - self.b

    def get_multiply(self):
        return self.a * self.b
    
    def get_division(self):
        return self.a / self.b

    def luke_index(self):
        ans = (self.a + self.b) * self.luke + 100
        return ans

if __name__ == "__main__":
    myCalc = Calculator(a=247, b=12)
    print(myCalc.get_division())