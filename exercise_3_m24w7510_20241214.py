#Name: Aye Thida | Student Id : M24W7510
#1.	Ask the user to input two lists of items (separated by spaces).
#2.	Convert the lists into sets.
#3.	Remove all items from the first set that are also in the second set.
#4.	Print the updated first set.
val_f = input("Enter first list: ")
val_fSet = {str(x) for x in val_f.split(" ")}
#val_sSet = input("Enter first list: ")
#print("First inputte list : ",val_fSet)
val_s = input("Enter Second list: ")
val_sSet = {str(x) for x in val_s.split(" ")}
#print( "Second inputte list : ",val_sSet)
for x in val_fSet.copy():
  if x in val_sSet:
    val_fSet.remove(x)
print("Updated set: ",val_fSet)