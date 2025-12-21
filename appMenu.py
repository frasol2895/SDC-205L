from datetime import datetime

print("frasol2895's Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable called option.
option = input()

print("You selected", option, "at", str(datetime.now()))
