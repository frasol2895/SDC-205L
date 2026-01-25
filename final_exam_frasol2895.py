# Frank Solomon
# Student ID: frasol2895
# Final Performance Assessment
# Date: January 25, 2026

from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference
import matplotlib.pyplot as plt


def askUser():
    total = 0

    # This loop runs five times to collect five numbers from the user
    # and adds each number to the running total
    for i in range(5):
        num = int(input("Enter a number: "))
        total += num

    print("The total of the five numbers is:", total)


def askIncome():

    # This loop runs five times to collect names and annual incomes
    # and appends each entry as a new line to the existing CSV file
    with open(r"C:\FinalExam\final.csv", "a") as file:
        for i in range(5):
            name = input("Enter a name: ")
            income = int(input("Enter annual income: "))
            file.write(f"{name},{income}\n")


def excelPie():
    names = []
    incomes = []

    with open(r"C:\FinalExam\final.csv", "r") as file:
        for line in file:
            data = line.strip().split(",")
            names.append(data[0])
            incomes.append(int(data[1]))

    # Create a new Excel workbook
    wb = Workbook()

    # Select the active worksheet
    ws = wb.active

    # Add headers to the worksheet
    ws.append(["Name", "Income"])

    # Add each name and income to the worksheet
    for i in range(len(names)):
        ws.append([names[i], incomes[i]])

    # Create a PieChart object
    pie = PieChart()

    # Define the data range for the chart
    data = Reference(ws, min_col=2, min_row=1, max_row=len(incomes) + 1)

    # Define the category labels for the chart
    labels = Reference(ws, min_col=1, min_row=2, max_row=len(names) + 1)

    # Add data to the pie chart
    pie.add_data(data, titles_from_data=True)

    # Set the labels for the pie chart
    pie.set_categories(labels)

    # Set the title of the pie chart
    pie.title = "frasol2895 January 25, 2026"

    # Add the pie chart to the worksheet
    ws.add_chart(pie, "E2")

    # Save the Excel file
    wb.save(r"C:\FinalExam\final.xlsx")


def verticalBar():
    names = []
    incomes = []

    with open(r"C:\FinalExam\final.csv", "r") as file:
        for line in file:
            data = line.strip().split(",")
            names.append(data[0])
            incomes.append(int(data[1]))

    plt.bar(names, incomes)
    plt.title("frasol2895 January 25, 2026")
    plt.xlabel("Name")
    plt.ylabel("Income")
    plt.show()


askUser()
askIncome()
excelPie()
verticalBar()
