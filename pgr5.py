#Splitting and Joining Strings
text = "Apple,Banana,Cherry"

# Splitting
fruits = text.split(", ")
print(fruits)  # Output: ['Apple', 'Banana', 'Cherry']

# Joining
new_text = " - ".join(fruits)
print(new_text)  # Output: "Apple - Banana - Cherry"