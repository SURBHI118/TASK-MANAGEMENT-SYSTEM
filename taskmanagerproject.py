import datetime

# Function to handle user signup
def signup():
    print("Please enter the username you want to use: ")
    username = input("Enter here: ")
    password = input("Enter a password: ")
    user_information(username, password)
    print("Sign up successful. Please proceed to log in.")
    login()

# Function to handle user login
def login():
    print("Please enter your username: ")
    user_nm = input("Enter here: ")
    pssd_wr = input("Enter the password: ") + '\n'

    try:
        usernm = user_nm + "_task.txt"
        with open(usernm, 'r') as f_:
            k = f_.readlines()[0]

        if pssd_wr == k:
            print("1--to view your data \n2--To add task \n3--Update task \n4--View task status")
            option = input("Select an option: ")

            if option == '1':
                view_data(usernm)
            elif option == '2':
                task_information(usernm)
            elif option == '3':
                task_update(user_nm)
            elif option == '4':
                task_update_viewer(user_nm)
            else:
                print("Invalid option!")

        else:
            print("Incorrect password!")
            login()

    except FileNotFoundError:
        print("User not found. Please sign up.")
        signup()

    except Exception as e:
        print("An error occurred:", e)
        login()

# Function to view user data
def view_data(username):
    with open(username, 'r') as ff:
        print(ff.read())

# Function to add task information
def task_information(username):
    print("Enter the number of tasks you want to add: ")
    num_tasks = int(input())

    with open(username, 'a') as f1:
        for i in range(1, num_tasks + 1):
            task = input("Enter task " + str(i) + ": ")
            target = input("Enter target " + str(i) + ": ")
            f1.write("TASK " + str(i) + ': ' + task + '\n')
            f1.write("TARGET " + str(i) + ": " + target + '\n')

# Function to update task status
def task_update(username):
    username = username + "_task.txt"
    print("Enter the tasks which are completed: ")
    task_completed = input()
    print("Enter tasks which are still not started: ")
    task_not_started = input()
    print("Enter tasks which you are doing: ")
    task_ongoing = input()

    with open(username, 'a') as fw:
        current_time = str(datetime.datetime.now())
        fw.write(current_time + '\n')
        fw.write("COMPLETED TASK:\n" + task_completed + '\n')
        fw.write("ONGOING TASK:\n" + task_ongoing + '\n')
        fw.write("NOT YET STARTED:\n" + task_not_started + '\n')

# Function to view task status
def task_update_viewer(username):
    ussnm = username + "_task.txt"
    with open(ussnm, 'r') as o:
        print(o.read())

# Function to handle user information
def user_information(ussnm, pssd):
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    age = input("Enter your age: ")
    ussnm_ = ussnm + "_task.txt"

    with open(ussnm_, 'a') as f:
        f.write(pssd + '\n')
        f.write("Name: " + name + '\n')
        f.write("Address: " + address + '\n')
        f.write("Age: " + age + '\n')

# Main function
if __name__ == '__main__':
    print("WELCOME TO SURBHI'S TASK MANAGER")
    print("Are you new to this software?")
    a = int(input("Type 1 if new, otherwise press 0: "))

    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have provided wrong input!")