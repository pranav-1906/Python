tasks = []
valid_choices = [1,2,3,4]
print("------TO-DO LIST------")
while True:
    print("1.Add a new task \n2.Remove task \n3.Show Tasks \n4.Quit")
    while True:
        try:
            choice = int(input("Enter your choice:"))
            if choice in valid_choices:
                break
            else:
                print("Invalid input!")
        except:
            print("Please enter a valid choice!")
    if choice == 1:
        print("------ADD TASK------")
        add = input("Enter a task:")
        if add.strip() == "":
            print("Task can't be empty!")
        else:
            tasks.append(add)
            print("Task added successfully!")
        print("------------")
    elif choice == 2:
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    print("Task removed successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a number!")
        else:
                print("No tasks to remove!")
        print("------------")
    elif choice == 3:
        if tasks:
            for index, task in enumerate(tasks, start = 1):
                print(f"{index}. {task}")
        else:
            print("No tasks in list!")
        print("------------")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid input!")