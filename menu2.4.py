from datetime import datetime

# Application title (FIRST output)
student_id = "frasol2895"
print(f"{student_id}'s Spreadsheet Automation Menu")

# Menu options stored in a data structure
menu_options = {
    1: "Input Data",
    2: "View Current Data",
    3: "Generate Report"
}

print("Choose a number from the following options")

# Print menu using a for-loop
for option, description in menu_options.items():
    print(f"{option} {description}")

# Get user input
choice = int(input())

# Validate input
if choice in menu_options:
    current_time = datetime.now()
    print(f"You selected {choice} at {current_time}")
else:
    print("Error: invalid choice selected")
