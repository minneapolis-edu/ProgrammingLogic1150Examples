"""
Making a to do list in Python using a while loop to get
the tasks, and a for loop to print all the tasks.
Also, print the total number of tasks.
"""

todo_list = []  # Make an empty list

while True:
    task = input('Enter your task, or press enter to stop: ')
    if task:   # An empty string is False
        todo_list.append(task)   # Add task to end of todo_list
    else:
        break   # If user entered an empty string, end the loop

print('Thank you. Your tasks are:')

for task in todo_list:  # For every task in the todo_list,
    print(task)         # print the task.

number_of_tasks = len(todo_list)
print(f'You have {number_of_tasks} tasks to do.')



