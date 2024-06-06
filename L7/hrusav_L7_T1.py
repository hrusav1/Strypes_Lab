class Fibs:
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib


"""
if __name__ == "__main__":
    fibs = Fibs()
    for f in fibs:
        if f > 1000:
            print(f)
            break
"""
