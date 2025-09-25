import time


class CountDown:
    def __init__(self, stop: int, direction: str):
        self.stop = stop
        self.direction = direction
   
    def __iter__(self):
        self.start = 1 if self.direction == "up" else self.stop 
        return self
    
    def __next__(self):
        if self.direction == "up":
            if self.start <= self.stop:
                value = self.start
                self.start += 1
                return value
            else:
                raise StopIteration
        
        elif self.direction == "down":
            if self.start >= 1:
                value = self.start
                self.start -= 1
                return value
            else:
                raise StopIteration
        
        else:
            raise ValueError("Invalid direction: choose 'up' or 'down'")
        

new = CountDown(5, "down")

temp = iter(new)

print(next(temp, "Out of range"))
print(next(temp, "Out of range"))
print(next(temp, "Out of range"))
print(next(temp, "Out of range"))
print(next(temp, "Out of range"))



print()
print("next printing for up")
time.sleep(2)

print()
new = CountDown(5, "up")

temp = iter(new)

print(next(temp, "Out of range"))
print(next(temp, "Out of range"))
print(next(temp, "Out of range"))
print(next(temp, "Out of range"))
print(next(temp, "Out of range"))






