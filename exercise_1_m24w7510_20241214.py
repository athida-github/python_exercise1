#Name: Aye Thida | Student Id : M24W7510
##Exercise 1: List: Count Numbers Greater Than 50
#1.	Ask the user to input a list of numbers (separated by spaces).
#2.	Count how many numbers in the list are greater than 50 and print the result.

count_gt50 = 0
input_str = input("Enter numbers: ")
#val_arr[0] = int(input_str.split(" "));
val_arr = [int(x) for x in input_str.split(" ")]
print(val_arr)
for x in val_arr:
 if x >= 50 :
  count_gt50+=1
print("Numbers greater than 50: ",count_gt50 )