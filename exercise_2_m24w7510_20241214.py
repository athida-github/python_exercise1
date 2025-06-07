#Name: Aye Thida | Student Id : M24W7510
#1.	Create a dictionary with items as keys and their quantities as values.
#2.	Allow the user to input an item name.
#3.	Print whether the item is in stock or not.
#ent_item= ""
stock_dict = {"apple": 10, "orange":0, "strawberry":50}
print(stock_dict)
ent_item = input("Enter operation value : ")
#print(ent_item)
if ent_item in stock_dict:
 if stock_dict[ent_item]<=0:
  print(ent_item,"is out of stock!")
 else:print(ent_item, "is avaiable!")
else: print("Out of inventory!")