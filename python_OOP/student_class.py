class Student:

    #points = int(input("Enter score: "))
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Scores = []

    def full_name(self):
        return f"{self.FirstName} {self.LastName}"
    

        
    def total_score(self):
        return sum(self.Scores)
    
    def add_new_score(self, points):
        self.Scores.append(points)
        return
    
    def max_score(self):
        return max(self.Scores)
    
    def min_score(self):
        return min(self.Scores)
    

        
iceking = Student("Ice", "King")

iceking.add_new_score(10)


iceking.add_new_score(20)
iceking.add_new_score(7)
iceking.add_new_score(8)



print(iceking.max_score())