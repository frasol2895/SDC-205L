from datetime import datetime

# This function displays the menu and controls program flow
def main():
    student_id = "frasol2895"

    while True:
        print(f"\n{student_id}'s Spreadsheet Automation Menu")

        menu_options = {
            1: "Input Data",
            2: "View Current Data",
            3: "Generate Report",
            4: "Exit"
        }

        print("Choose a number from the following options")
        for option, description in menu_options.items():
            print(f"{option} {description}")

        choice = int(input())

        if choice == 1:
            getInput()
        elif choice == 2:
            viewData("ZooData.csv")
        elif choice == 3:
            current_time = datetime.now()
            print(f"Generate Report selected at {current_time}")
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Error: invalid choice selected")


# This function handles multiple user inputs and sends data to insertData
def getInput():
    entries = int(input("How many entries would you like to add? "))

    for _ in range(entries):
        date = input("Enter a date: ")
        high_temp = input("Enter the highest temp for the inputted date: ")

        data = f"{date},{high_temp}"
        insertData("ZooData.csv", data)


# This function inserts comma-separated data into a CSV file
def insertData(path, data):
    try:
        with open(path, "a") as file:
            file.write(data + "\n")

        current_time = datetime.now()
        print(f"The following data was saved at {current_time}")
        print(data)

    except Exception as e:
        print("Error writing to file:", e)


# This function reads and displays data from a CSV file
def viewData(path):
    try:
        print(f"\nThe file {path}")
        with open(path, "r") as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print("Error reading file:", e)


main()
