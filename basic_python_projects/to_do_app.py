
def task():
    tasks = []
    print("Wellcome to task management system!!__")
    total_task=int(input("Enter the tasks you want to add!"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task{i}")
        tasks.append(task_name)

    print(f"Today,s tasks are\n{tasks}")    
    while True:
        operation= int (input("Enter 1-Add\n2-Update\n3-Dlete\n4-View\n5-Exit/Stop/"))
        if operation ==1:
            add =input("Enter task you want to Add! ")
            tasks.append(add)
            print(f"Task {add} has been succesfully added...")

        elif operation ==2:
            updated_val=input("Enter the val you want to updated!= ")
            if updated_val in tasks:
                up =input("Enter the new Task =")
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print(f"updated task {up}")

        elif operation ==3:
            del_val=input("Which task you want to delete!")
            if del_val in tasks:
                ind =tasks.index(del_val)  
                del tasks[ind]
                print(f"Task {del_val} has been deleted!")  

        elif operation == 4:
            print(f"total tasks = {tasks}")  

        elif operation == 5:
            print("Closing the program")
            break
        else:
            print("Invalid Input!")           

task()    
          



