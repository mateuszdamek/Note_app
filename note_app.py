
my_list = []
choice = int(input("[1] - add item\n[2] - delete item\n[3] - show list\n"))

while(True):
    if(choice != 1 and choice != 2 and choice != 3):
        print("Wrong select.")
        choice = int(input("[1] - add item\n[2] - delete item\n[3] - show list\n"))
    else:
        match(choice):
            case 1: #add
                add_element = input("Add: ")
                my_list.append(add_element + "\n")

            case 2: #delete
                if(len(my_list) > 0):
                    i = 1
                    for elements in my_list:
                        print(f"[{i}] " + elements, end="")
                        i += 1
                    delete_element = int(input('Choose element to remove: '))
                    my_list.pop(delete_element - 1)
                else:
                    print("No elements to remove.")

            case 3: #show
                if(len(my_list) > 0):
                    i = 1
                    for elements in my_list:
                        print(f"[{i}] " + elements, end="")
                        i += 1
                else:
                    print("No elements.")

    choice = int(input("[1] - add item\n[2] - delete item\n[3] - show list\n"))
