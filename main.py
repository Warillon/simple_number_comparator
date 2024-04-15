def comparator():
    while True:
        print("________________________________")

        print("    SIMPLE NUMBER COMPARATOR    ")

        print("--------------------------------")


        while True:
            firstNumber = input("Enter the first number   : ")
            try:
                firstNumber = float(firstNumber)
                break
            except ValueError:
                print("*Enter a valid number.*")
                print(" ")
                print(" ")

        while True:
            secondNumber = input("Enter the second number  : ")
            try:
                secondNumber = float(secondNumber)
                break
            except ValueError:
                print("*Enter a valid number.*")
                print(" ")
                print(" ")
    
        print("--------------------------------")

        firstNumber = float(firstNumber)
        secondNumber = float(secondNumber)

        if firstNumber > secondNumber:
            print(f"{firstNumber} is greater than {secondNumber}.")

        if secondNumber > firstNumber:
            print(f"{secondNumber} is greater than {firstNumber}.")

        if firstNumber == secondNumber:
            print(f"{firstNumber} and {secondNumber} are equal.")

        print("________________________________")
    
        continue_choice = input("Continue comparing? (Y/N) ").upper()
        if continue_choice != "Y":
            break

comparator()

# Write by Albert GRAUENFELS (Warillon, 2024)
# SPDX_License-Identifier: CC-BY-NC-4.0
