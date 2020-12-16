# Value error check of the first entered operator + checks whethere operants and operators are entered by order
while True:
    element = (input("Enter the operator: "))

    try:
        element = int(element)

    except ValueError:
        print(f"operator {element} is not a number")

    else:
        break

# Operant check (checks whethere operants and operators are entered by order)
while True:

    operant = input("Enter the operant: ")

    while operant not in "+-*/=" or operant == "":
        operant = input("Enter the operant: ")

    if operant == "=":
        break
# Check Value Error for operators + checks whethere operants and operators are entered by order
    while True:
        operator = (input("Enter the operator: "))

        try:
            operator = int(operator)

        except ValueError:
            print(f"operator {operator} is not a number")

        else:
            break
# Calculation part
    if operant == "+":
        element += operator

    elif operant == "-":
        element -= operator

    elif operant == "*":
        element *= operator

    elif operant == "/":
        # Check Zero Division Error
        while operator == 0:

            try:
                element /= operator

            except ZeroDivisionError:

                print("Zero Division Error")
                operator += float(input("Enter the operator: "))

            else:
                break

        element /= operator
# Print Solution
print(int(element))
