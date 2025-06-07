#Name: Aye Thida | Student Id : M24W7510
#1.	Ask the user to input a list of numbers (separated by spaces).
#2.	Create two separate lists: one for even numbers and one for odd numbers.
#3.	Print both lists.
input_list = input("Enter first list: ")
val_even=list()
val_odd=list()
val_list =[int(x) for x in input_list.split(" ")]
#print(val_list)
for x in val_list:
 if x%2 == 0:
  val_even.append(x)
 else:
  val_odd.append(x)
print("Even numbers:",val_even)
print("Odd numbers:",val_odd)