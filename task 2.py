#-----------the shopping list maker ----


grocery_list=()
grocery_history=[]
def grocery_add(): 
    needs_items = True
    while needs_items == True:
        
        print("what would you like to add? ")
        name=input("Name: ")

        grocery_list={'item_name':name}
        grocery_history.append(grocery_list)
        break


def remove_items(): 
    global grocery_list 
    item_to_remove = input("Which item do you want to remove? ")() 
    newlist = grocery_list.copy() 
    for item in grocery_list:
        if item() == item_to_remove:
            newlist.remove(item) 
    grocery_list = newlist




 


    

