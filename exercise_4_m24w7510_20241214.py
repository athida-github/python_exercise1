#Name: Aye Thida | Student Id : M24W7510
#1.	Ask the user to enter a sentence.
#2.	Split the sentence into words and store them in a list.
#3.	Reverse the order of words in the list and print the result.
val_sentence = input("Enter a sentence: ")
#reverse_num = int(str(input_num)[::-1])
val_list = [str(x) for x in val_sentence.split(" ")[::-1]]
#print(val_list)
for x in val_list:
  print(x,end=" ")