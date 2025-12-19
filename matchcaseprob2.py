i = int(input("Enter the First Number:"))
j = int(input("Enter the Second Number:"))

operation = input("Choose the operation : + , - , * , / , % , ** , // , square , cube :\n")

match operation:
    case "+":
        print(i + j)
    case "-":
        print(i - j)
    case "*":
        print(i * j)
    case "/":
        print(i / j)
    case "**":
        print(i ** j)
    case "//":
        print(i // j)
    case "square":
        print(i * i , j * j)
    case "cube":
        print(i * i * i , j * j * j)
