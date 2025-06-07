#Name: Aye Thida | Student Id : M24W7510
#1.	Create a dictionary with 5 students’ names as keys and their grades as values.
#2.	Allow the user to enter a student’s name.
#3.	Print the student’s grade or indicate if the student is not found.
student_dict = {"Alice": 60, "Wendy":20, "Henry":50,"Sunny":100 }
print(student_dict)
search_std = input("Enter student name: ")
#print(ent_item)
if search_std in student_dict:
 print("Grade: ", student_dict[search_std])
else:print("Student not found.")