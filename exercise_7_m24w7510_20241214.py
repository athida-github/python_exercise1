#Name: Aye Thida | Student Id : M24W7510
#1.	Create a set containing numbers from 1 to 10.
#2.	Ask the user to input numbers they have (separated by spaces).
#3.	Find and print the numbers that are missing.

val_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(val_set)
input_val = input("Enter numbers: ")
input_set = {int(x) for x in input_val.split(" ")}
#print(input_set)
new_set=set()
for x in val_set.copy():
 if x not in input_set:
  new_set.add(x)
print("Missing numbers: ",new_set)