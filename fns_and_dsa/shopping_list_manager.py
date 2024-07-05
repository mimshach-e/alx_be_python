#  Task 1 - Shopping List Manager

# Core Functionality:
# shopping_list = []

# def add_item(item_number, item_name, item_price):
#     shopping_list_item = {
#         "item_number": item_number,
#         "item_name": item_name,
#         "item_price": item_price
        
#     }
#     shopping_list.append(shopping_list_item)
#     print(f"Shopping item '{shopping_list_item}' added to the list successfully")


# def remove_item(shopping_list, item_name):
#     for shopping_list_item in shopping_list:
#         if shopping_list_item["item_name"]:
#             shopping_list.remove(shopping_list_item)
#             print(f"{item_name} removed successfully")
#             return
#     print(f"{item_name} not found!")

# def view_item(shopping_list):
#     if not shopping_list:
#         print("No item found!")

#     for shopping_list_item in shopping_list:
#         print("My Shopping List")
#         print(f"{shopping_list_item["item_number"]}. {shopping_list_item["item_name"]} - Price: ${shopping_list_item["item_price"]}")



def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
             # Prompt for and add an item
            item_name = input("Enter the item to add: ")
            shopping_list.append(item_name)
            print(f"The item '{item_name}' is added successfully.")  
          
        elif choice == '2':
            # Prompt for and remove an item
            item_name = input("Enter the name of the item to remove: ")
            shopping_list.remove(item_name)
            print(f"{item_name} is removed from the list successfully.")

        elif choice == '3':
            # Display the shopping list
            print("My Shopping List")
            for item_name in shopping_list:
                print(f"{item_name}.")
            
            if not shopping_list:
                print("Item not found!")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()        



       
                



