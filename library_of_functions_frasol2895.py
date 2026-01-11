# Library of Functions Performance Assessment
# Student ID: frasol2895

def functionOne():
    print("My Student ID is frasol2895")

def functionTwo():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    sumResult = n1 + n2
    print(f"The sum of {n1} and {n2} is {sumResult}")
    return sumResult

def functionThree(sumValue):
    if sumValue > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    return 2895

def main():
    # Call functionOne to display the student ID
    functionOne()

    # Call functionTwo and store the returned sum
    returnedSum = functionTwo()

    # Call functionThree and store the returned student ID number
    returnedID = functionThree(returnedSum)

    # Display the value returned from functionThree
    print(f"functionThree returned the value of {returnedID}")

# Start the program by calling main
main()
