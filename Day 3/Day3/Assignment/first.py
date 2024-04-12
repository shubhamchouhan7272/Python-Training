# define 3 functions "add()","modify()" and "delete()" with just a print message.
# now accept input from user as a number. if the number entered is 1, call "add()"
# if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]

def add():
    print("Add Something...")

def  modify():
    print("Modify Something...")

def delete():
    print("Delete Something...")

def main():
    while True:
        try:
            choice = int(input("Enter 1 for adding, 2 for modify and 3 for delete (or 0 to exit...) : "))
            break
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, 3 or 0).")

    match choice:
        case 1:
            add()

        case 2:
            modify()

        case 3:
            delete()

        case 0:
            print("Exiting...") 
            exit()
        case _:
            print("Invalid choice. Please enter a number (1, 2, 3 or 0).")

if __name__ == "__main__":
    main()
