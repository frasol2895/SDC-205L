# Student ID: frasol2895
# Spreadsheet Automation Project – Temperature (F to C)

from datetime import datetime


# convertData(value) -> float
# Argument: value (float) representing temperature in Fahrenheit
# Return: converted temperature in Celsius
def convertData(value):
    return (value - 32) * 5 / 9


def getInput():
    entries = int(input("How many entries are you inputting?\n"))

    for _ in range(entries):
        print("Enter a date:")
        dateEntered = input()

        print("Enter the highest temp for the inputted date:")
        tempF = float(input())

        # convertData(value) -> float
        # Argument: temperature in Fahrenheit
        # Return: temperature converted to Celsius
        tempC = convertData(tempF)

        print(
            f"The following was saved at {datetime.now()} :\n"
            f"{dateEntered},{int(tempF)},{tempC}"
        )


def main():
    print("frasol2895's Spreadsheet Automation Menu")
    print("Choose a number from the following options")
    print("1 Input Data")
    print("2 View Current Data")
    print("3 Generate Report")

    choice = input()

    print(f"You selected {choice} at {datetime.now()}")

    if choice == "1":
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")


main()
