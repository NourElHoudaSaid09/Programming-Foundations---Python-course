#Nour El Houda Said
#final project 
#Foundation of python



tasks = [
    {'name' : 'Write email to Jan', 'completed' : True},
    {'name' : 'Sweep front porch', 'completed' : True},
    {'name' : 'Call mom', 'completed' : False}
]

def list_tasks():
    for index, task in enumerate(tasks):
        print(str.format('{}: {} (Completed: {})', index, task['name'], task['completed']))


def add_task():
    task_text = input('Please add a task: ')

    # Using the above task_text variable, create a dictionary named new_task and set completed to False
    new_task = {'name':task_text,'completed':False}
    # Then, add new_task to the tasks list
    tasks.append(new_task)
    #list_tasks()

# You will need a function to handle removing a task.
def remove_task():
    # When this function is run, list out the tasks. Hint! There is already a function that handles this
    list_tasks()
    # Here, create a variable that uses input. The user should be able to input the index number of the task to be removed. 
    # Hint! You will need to wrap the input() function within the int() function so the user's input is read as a number.
    task_index=int(input('\nWhich task do you need to delete? (Just type the number of the task): '))
    # Here, delete the task in the tasks list based on the above variable
    del tasks[task_index]
    #list_tasks()

# You will need a function to handle marking a task complete.
def is_completed():
    # When this function is run, list out the tasks. Hint! There is a function that already does this for you.
    list_tasks()
    # Here, create a variable that uses input. The user should be able to input the index number of the task to be marked complete.
    #  Hint! You will need to wrap the input() function within the int() function so the user's input is read as a number.
    task_index=int(input('\nWhich task did you complete? (Just type the number of the task): '))
    # Mark the task complete in the tasks list based on the variable you created above.
    #  Hint! you will need to use two sets of square brackets to find the index and set the appropriate key to True 
    tasks [task_index]['completed']=True
    #list_tasks()
    
menu_text = """
====================
1. List the tasks
2. Add a task
3. Remove a task
4. Mark task complete
5. Quit

What would you like to do? """

program_is_running = True

while program_is_running:
    decision = input(menu_text)
    if decision == '1':
        list_tasks()

    # Add elif statements for inputs 2, 3, and 4
    elif decision == '2':
        #add a task
        add_task()
    elif decision == '3':
        #remove a task by a specific index
        remove_task()
    elif decision == '4':
        #mark a task as completed
        is_completed()
    elif decision == '5':
        program_is_running = False
    else:
        print('please choose a valid option')
