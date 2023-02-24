from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy()
    # update lastActivity with the current datetime value
    task['lastActivity'] = datetime.now()
    # set the name, description, and due date (all must be provided)
    if name and description and due:
        # due date must match one of the formats mentioned in str_to_datetime()
        task['name'] = name
        task['description'] = description
        task['due'] = str_to_datetime(due)
        tasks.append(task)
        print(f"Task {name} added successfully!")
    else:
        print("Failed to add task due to missing data.")
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    if index >= len(tasks):
        print("Invalid index.")
        return
    task = tasks[index]
    print(f"Update Task {task['name']}:")
    name = input(f"What's the name of this task? ({task['name']}) \n").strip() or task['name']
    desc = input(f"What's a brief descriptions of this task? ({task['description']}) \n").strip() or task['description']
    due = input(f"When is this task due (format: m/d/y H:M:S) ({task['due']}) \n").strip() or task['due']
    update_task(index, name=name, description=desc, due=due)


def update_task(index: int, name: str = None, description:str = None, due: str = None):
    """ 
    Updates the name, description , due date of a task found by index if an update to the property was provided 
    """
    tasks = load()

    if index >= len(tasks) or index < 0:
        print("Invalid index. Please enter a number within range.")
        return

    if name is not None:
        tasks[index]['name'] = name
    if description is not None:
        tasks[index]['description'] = description
    if due is not None:
        tasks[index]['due'] = due

    tasks[index]['lastActivity'] = str(datetime.datetime.now())

    if name is None and description is None and due is None:
        print("Task was not updated")
    else:
        print("Task updated")

    save(tasks)

def mark_done(index):
    """ 
    Updates a single task, via index, to a done datetime 
    """
    tasks = load()

    if index >= len(tasks) or index < 0:
        print("Invalid index. Please enter a number within range.")
        return

    if 'done' in tasks[index] and tasks[index]['done'] is not None:
        print("Task already completed")
    else:
        tasks[index]['done'] = str(datetime.datetime.now())
        print("Task marked as done")

    save(tasks)

def view_task(index):
    """ 
    View more info about a specific task fetch by index 
    """
    tasks = load()

    if index >= len(tasks) or index < 0:
        print("Invalid index. Please enter a number within range.")
        return

    task = tasks[index]
    completed = task.get('done', "-")
    done = 'x' if completed != "-" else ' '
    
    print(f"""[{done}] Task: {task['name']}
    Description: {task['description']}
    Last Activity: {task['lastActivity']}
    Due: {task['due']}
    Completed: {completed}""")

def delete_task(index):
    """ 
    Deletes a task from the tasks list by index 
    """
    tasks = load()

    if index >= len(tasks) or index < 0:
        print("Invalid index. Please enter a number within range.")
        return

    tasks.pop(index)

    print("Task deleted")

    save(tasks)

def get_incomplete_tasks():
    """ 
    Prints a list of tasks that are not done 
    """
    tasks = load()
    incomplete_tasks = [task for task in tasks if task.get('done') is None]
    list_tasks(incomplete_tasks)

def get_overdue_tasks():
    """ 
    Prints a list of tasks that are over due completion (not done and expired) 
    """
    tasks = load()
    overdue_tasks = [task for task in tasks if task.get('done') is None and datetime.datetime.now() > datetime.datetime.strptime(task['due'], '%Y-%m-%d %H:%M:%S.%f')]
    list_tasks(overdue_tasks)


def get_time_remaining(index, tasks):
    """
    Outputs the number of days, hours, minutes, seconds a task has before it's overdue
    otherwise shows similar info for how far past due it is.

    :param index: int, the index of the task to check
    :param tasks: list, a list of dictionaries containing the tasks and their due dates
    """
    if index < 0 or index >= len(tasks):
        print("Invalid index. Please provide an index within the range of tasks.")
        return
    
    task = tasks[index]
    due_date = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    time_diff = due_date - now
    
    if time_diff.total_seconds() < 0:
        time_diff = abs(time_diff)
        overdue = True
        message = "Task is overdue by"
    else:
        overdue = False
        message = "Time remaining:"
    
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if overdue:
        print(f"{message} {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    else:
        print(f"{message} {days} days, {hours} hours, {minutes} minutes, {seconds} seconds until the task is due.")
        
command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
#if __name__ == "__main__":
run()

