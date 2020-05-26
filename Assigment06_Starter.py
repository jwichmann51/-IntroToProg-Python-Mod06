# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# JWichmann, 5/22/2020, Reviewed code ahead of the Friday evening Zoom with Dave
# JWichmann, 5/24/2020, Modified code to complete assignment
# JWichmann, 5/25/2020, Final code review before submission
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        # This is a function with two parameters:
        # i) file_name (strFileName which is ToDoFile.txt)
        # and
        # ii) list_of_rows (lstTable)
        # This function is activated in Step 1 below via the code Processor.read_data_from_file(strFileName, lstTable)
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(strTask, strPriority, list_of_rows):
        # This is a function with three parameters:
        # i) strTask which is the task inputted by the user
        # ii) strPriority which is the priority inputted by the user
        # iii) list_of_rows (lstTable)
        # This is the part of the code that does the processing.  The Presentation section below is where the user enters the data.
        # This function is activated by Processor.add_data_to_list(strTask, strPriority, lstTable)
        # TODO: Add Code Here!  ++2) Add a new item ++ DONE
        strTask = str(input(" Enter a Task: "))
        strPriority = str(input(" Enter the Priority: "))
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        #lstTable.append({"Task": strTask, "Priority": strPriority})
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(strTask, list_of_rows):
        # This is a function with two parameters:
        # i) task (strTask)
        # ii) list_of_rows (lstTable)
        # This code is run with the command Processor.remove_data_from_list(strTask, lstTable)
        # TODO: Add Code Here! ++3) Remove an existing item++ DONE
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)
                print("row removed")
                print(lstTable, '<< List with Dictionary objects')
            else:
                print("row not found")
                print(lstTable, '<< List with Dictionary objects')
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # This code will be called with the following code below Processor.write_data_to_file(strFileName, lstTable)
        # TODO: Add Code Here! ++4) Save data to file ++ DONE
        objFile = open("ToDoFile.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ',' + str(row["Priority"] + '\n'))
        objFile.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        # This is a function with one parameter:
        # i) list_of_rows (lstTable)
        # This function is activated by Processor.print_current_Tasks_in_list(lstTable)
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        pass  # TODO: Add Code Here! DONE
        print(" Type in a Task and Priority")
        # strTask = str(input(" Enter a Task: "))
        # strPriority = str(input(" Enter the Priority: "))
        # return task, priority

    @staticmethod
    def input_task_to_remove():
        pass  # TODO: Add Code Here! DONE
        strTask = input("Task to Remove: ")
        # return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here DONE
        IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask, strPriority, lstTable) 
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here DONE
        IO.input_task_to_remove()
        Processor.remove_data_from_list(strTask, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here! DONE
            Processor.write_data_to_file(strFileName, lstTable)
            print(" Data was saved!")
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Add Code Here! DONE
            IO.print_current_Tasks_in_list(lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
