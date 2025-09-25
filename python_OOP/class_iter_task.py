

class Iterator:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        if self.x < len( ):
            y = self.x
            self.x += 1
            return y
        else:
            raise
    

print(next(temp))
print(next(temp))
print(next(temp))




