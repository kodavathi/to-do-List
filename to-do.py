tasks=[]
while True:
    print("\nOptions:\n1. Display to-do list\n2. Add a task\n3. Mark a task as completed\n4. Remove a task\n5. Quit")
    c=int(input("Enter your choice: "))
    #Display to-do list
    if(c==1):
        if(c==1):
            if(tasks==[]):
                print("Your to-do list is empty.\n")
            else:
                for index, task in enumerate(tasks, start=1):
                    status="Done" if task["done"] else "Not Done"
                    print(f"{index}. {task['task']} ({status})")
                    
    #Add a task
    if(c==2):
        task=input("Enter the task: ")
        tasks.append({"task":task,"done":False})
        print("Task '%s' added to your to-do list."%task,"\n")

    #Mark a task as completed
    if(c==3):
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status="Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} ({status})")
        tindex=int(input("Enter the task number to mark as compleated: "))
        if 0 <= (tindex-1)<len(tasks):
            tasks[tindex-1]["done"]= True
            print("Task ",tindex," marked as completed.\n")
        else:
            print("Invalid task number. Please enter a valid task number.\n")

    #Remove a task
    if(c==4):
        print("To-Do List:")
        count=1
        for index, task in enumerate(tasks, start=1):
            status="Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} ({status})")
            count+=1
        tindex1=int(input("Enter the task number to remove: "))
        if 0 <= tindex1-1 <len(tasks):
            del(tasks[tindex1-1])
            print("Task '%s' is removed from your to-do list."%task['task'],"\n")
        else:
            print("Invalid task number. Please enter a valid task number.\n")
        

    #quit
    if(c==5):
        break
    
    if(c>=5):
        print("Invalid  choice.Please enter a valid option\n")
