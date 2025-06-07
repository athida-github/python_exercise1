#Name: Aye Thida | Student Id : M24W7510
#1.	Ask the user to input a sentence.
#2.	Create a dictionary where keys are the words from the sentence, and values are their lengths.
#3.	Print the dictionary.
input_str = input("Enter first list: ")
input_list=[str(x) for x in input_str.split(" ")]
val_dict=dict()
print("Enter a sentence: ",input_list)
for x in input_str.split(" "):
 val_dict[x]=len(x)
print("Word lengths: ",val_dict)