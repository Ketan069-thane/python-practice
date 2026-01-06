# function with user input
def average(a, b, c):
    avg = (a + b + c) / 3
    print("The average is:", avg)
average(int(input("Enter the numbers to find average:\nFirst number: ")),
        int(input("Second number: ")),
        int(input("Third number: ")))
