# ---------------------------------------------------------------------------- #
# Title: An Alpine Skiing Packing List
# Description: Demonstration of Pickling and Exception Handling
# ChangeLog: (Who,When,What):
# SPaulen, 12/01/2020, Created
# ---------------------------------------------------------------------------- #
# Import Pickle Module
import pickle

# Declare Variables and Classes
strFileName = "AlpineSki.txt" # The name of the text data file
strPickledFileName = "AlpineSki_Pickled.txt" # The name of the binary data file
lstTable = [] # A list that acts as a 'table' of rows
intChoice = 0 # Captures the user option selection
strStatus = "" # Captures the status of an processing functions


# Exception
class InvalidChoice(Exception):
    def __str__(self):
        return 'Please enter  1, 2 or 3' + "\n"


# Processing
class Processor:
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        list_of_rows.clear()  # clear current data
        try:
            file = open(file_name, "r")
            for row in file:
                if "\n" in row:
                    row = row.replace("\n", " ")
                list_of_rows.append(row)
            file.close()
            return list_of_rows, "Success"
        except:
            return None, "Success"

    @staticmethod
    def pickle_to_file(list_of_rows, file_name):
        file = open(file_name, 'wb')
        pickle.dump(list_of_rows, file)
        file.close()
        return list_of_rows, "Success"

    @staticmethod
    def unpickled_from_file(list_of_rows, file_name):
        file = open(file_name, "rb")
        list_of_rows = pickle.load(file)
        file.close()
        return list_of_rows, "Success"


# Presentation
class Presentation:
    @staticmethod
    def print_data_from_file(list_of_rows):
        print("******* Alpine Ski Packing List *******")
        for row in list_of_rows:
            print(row)
        print("*******+++++++++++++++++++++++++*******")

    @staticmethod
    def print_menu_tasks():
        print('''
        Menu of Options
        1) Pickle
        2) UnPickle
        3) Exit Program
        ''')


# Main Body
while True:
    try:
        Presentation.print_menu_tasks()
        intChoice = input("> ")
        if intChoice == 1:
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
            Presentation.print_data_from_file(lstTable)
            lstTable, strStatus = Processor.pickle_to_file(lstTable, strPickledFileName)
            print(strStatus + ": The File has been Pickled! ")
        elif intChoice == 2:
            lstTable, strStatus = Processor.unpickled_from_file(lstTable, strPickledFileName)
            Presentation.print_data_from_file(lstTable)
            print(strStatus + ": The File has been UnPickled! ")
        elif intChoice == 3:
            print("Goodbye!")
            break
        else:
            raise InvalidChoice()

    except Exception as e:
        print("The Python error message is: ")
        print(e, "\n")