#  Task 1 - Shopping List Manager

# Core Functionality:


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



       
                



