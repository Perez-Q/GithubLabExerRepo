class Student(object):
    """Represents a student."""
    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number): # count < number
            self.scores.append(0)
    def getName(self):
        """Returns the student's name."""
        return self.name
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score
    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def methods_scores(self, name1, name2):
        Ave1 = name1.getAverage()
        Ave2 = name2.getAverage()
        if(Ave1 < Ave2):
            return f"{name2.name} has a better score"
        elif(Ave1 > Ave2):
            return f"{name1.name} has a better score"
        elif(Ave1==Ave2):
            return f"Both scores are equal" 
        
    def methods_name(self,name1,name2):
        if(name1.name<name2.name):
            return f"{name2.name} has a bigger weight"
        elif(name1.name>name2.name):
            return f"{name1.name} has a bigger weight"
        elif(name1.name==name2.name):
            return f"Both names are equal"

def main():
    #Populate the students
    student1 = Student("Ken", 5) 
    student2 = Student("Abigail", 5)
    student1.setScore(5,86), student1.setScore(4,90), student1.setScore(3,89), student1.setScore(2,87), student1.setScore(1,84)
    student2.setScore(5,85), student2.setScore(4,88), student2.setScore(3,87), student2.setScore(2,90), student2.setScore(1,90)

    print(student1.methods_scores(student1, student2))
    print(student1.methods_name(student1, student2))

if __name__ == "__main__":
    main()
