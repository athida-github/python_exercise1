#Name: Aye Thida | Student Id : M24W7510
#1.	Ask the user to input a list of numbers (separated by spaces).
#2.	Find and print the second largest number in the list.

input_val = input("Enter numbers: ")
val_tup = tuple(int(x) for x in input_val.split(" "))
sorted_tup = sorted(val_tup)
print("Second largest number: ",sorted_tup[len(sorted_tup)-2])