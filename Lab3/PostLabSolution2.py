import random

class Student(object):
    """Represents a student."""
    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = [0] * number
    
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score
    
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def __str__(self):
        """Returns the string representation of the student."""
        return f"Name: {self.name}\nScores: {' '.join(map(str, self.scores))}"

def main():
    # Create several Student objects
    students = [
        Student("Ken", 5),
        Student("Abigail", 5),
        Student("Jayson", 5),
        Student("John", 5),
        Student("Kim", 5)
    ]

    # Set scores for each student
    students[0].setScore(1, 84); students[0].setScore(2, 87); students[0].setScore(3, 89); students[0].setScore(4, 90); students[0].setScore(5, 86)
    students[1].setScore(1, 90); students[1].setScore(2, 90); students[1].setScore(3, 87); students[1].setScore(4, 88); students[1].setScore(5, 85)
    students[2].setScore(1, 78); students[2].setScore(2, 82); students[2].setScore(3, 80); students[2].setScore(4, 79); students[2].setScore(5, 81)
    students[3].setScore(1, 91); students[3].setScore(2, 89); students[3].setScore(3, 93); students[3].setScore(4, 88); students[3].setScore(5, 87)
    students[4].setScore(1, 85); students[4].setScore(2, 88); students[4].setScore(3, 84); students[4].setScore(4, 83); students[4].setScore(5, 86)

    # Shuffle the list
    random.shuffle(students)

    # Sort the list by student name
    students.sort(key=lambda student: student.name)

    # Display each student's information
    for student in students:
        print(student)

if __name__ == "__main__":
    main()
