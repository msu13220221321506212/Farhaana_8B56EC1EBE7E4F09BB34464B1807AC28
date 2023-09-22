class Student:

  def __init__(self, name,roll_number, cgpa):
    self.name = name 
    self.roll_number = roll_number 
    self.cgpa = cgpa


def sort_students(student_list):
  #Sort the list of students in descendingorder of CGPA
  sorted_students = sorted(student_list, 
                     key=lambda student: student.cgpa,
                     reverse=True)
  return sorted_students


# Example usage:
students = [
   Student("Afreen", "A123", 1.5),
   Student("Sarah", "A124", 9.9),
   Student("Kaneeza", "A125", 9.5),
   Student("Raihaana", "A126", 4.5),
]

sorted_students = sort_students(students)

# Print the sorted list of students 
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))