oplist=[]


while True:
    print("\n---list of opearations---")
    print("1.insert an element at a position")
    print("2.remove an element")
    print("3.append an element")
    print("4.display the length of the list")
    print("5.pop an element")
    print("6.clear the list")
    print("7.display the list")
    print("8.Exit")

    choice=int(input("Enter your choice(1-8):"))

    if choice == 1:
        element=input("enter the element to insert:")
        pos=int(input("enter the position(index):"))
        oplist.insert(pos,element)
        print("updated list:",oplist)

    elif choice == 2:
        if element in oplist:
            element=input("enter the element to remove:")
            oplist.remove(element)
            print("updated list:",oplist)
        else:
            print("element not found in the list")

    elif choice == 3:
        element=input("enter the element to append:")
        oplist.append(element)
        print("updated list:",oplist)

    elif choice == 4:
        print("Display the length of the list:",len(oplist))

    elif choice == 5:
        if oplist:
            popped = oplist.pop()
            print(f"popped element:{popped}")
            print("updated list:",oplist)
        else:
            print("list is empty.nothing to pop")
    elif choice == 6:
        oplist.clear()
        print("list cleared.current_list:",oplist)

    elif choice==7:
        if oplist:
            print("current_list:",oplist)
        else:
            print(" list is empty")
    elif choice==8:
        print("exiting program.goodbye!")
        break

    else:
        print("Invalid choice! please enter number between 1 and 8")
            

                

