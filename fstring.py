# String Formatting using f-strings
template = "Dear {}, your current balance is {} USD. "
a = "Ketan"
a1 = 10000
b = "Sam"
b1 = 20000
print(f"Dear {a}, your current balance is {a1} USD. ")
print(f"Dear {b}, your current balance is {b1} USD. ")
print(template.format(a, a1))
print(template.format(b, b1))
