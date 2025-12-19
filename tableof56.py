#Here we will print the table for any number from 1 to 20 using for loop ---- #here we have took the range value upto 21 it means while reading python will execute it with ( n - 1)
# then for example if in range the number is starting from 1 and ending upto 21 it means then the table will start with 1 and end up with 20 
j = int(input("Enter any number to get the table of it till 20: \n"))
for i in range(1,21):
  print( j , " x ", i, "=" , j * i)
