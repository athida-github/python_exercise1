#Name: Aye Thida | Student Id : M24W7510
#1.	Create a dictionary with items as keys and prices as values.
#2.	Ask the user to enter the name of an item and the quantity sold.
#3.	Calculate and print the total sales value for the entered item.
item_dict = {"apple": 10, "orange":15, "gape":20}
result = 0
print("Items and prices:",item_dict)
input_item = input("Enter item: ")
input_qty = int(input("Enter quantity: "))
if input_item in item_dict:
 result = item_dict[input_item]*input_qty;
print("Total sales: ",result)