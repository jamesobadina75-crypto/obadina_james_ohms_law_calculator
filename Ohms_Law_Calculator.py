
# OHM'S LAW AND POWER CALCULATOR
# CTE 123 PROJECT
# MECHATRONICS ENGINEERING

# Function to collect valid numbers
def get_number(message):
    while True:
        try:
            number = float(input(message))

            if number <= 0:
                print("Error! Enter a number greater than zero.")
            else:
                return number

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to perform calculations
def calculate():
    global count

    print("\n===== OHM'S LAW CALCULATOR =====")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    # Calculate voltage
    if choice == "1":
        current = get_number("Enter current (A): ")
        resistance = get_number("Enter resistance (Ohms): ")

        voltage = current * resistance
        print("Voltage =", voltage, "Volts")

    # Calculate current
    elif choice == "2":
        voltage = get_number("Enter voltage (V): ")
        resistance = get_number("Enter resistance (Ohms): ")

        current = voltage / resistance
        print("Current =", current, "Amperes")

    # Calculate resistance
    elif choice == "3":
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ")

        resistance = voltage / current
        print("Resistance =", resistance, "Ohms")

    # Calculate electrical power
    elif choice == "4":
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ")

        power = voltage * current
        print("Power =", power, "Watts")

    # Exit the program
    elif choice == "5":
        print("Thank you for using the calculator!")
        return False

    else:
        print("Invalid option! Choose between 1 and 5.")
        return True

    # Count completed calculations
    count += 1
    print("Calculations completed:", count)

    return True


# Main program
count = 0

# Repeat the calculator until the user exits
while True:
    if calculate() == False:
        break

print("Total calculations:", count)
print("Program ended.")
