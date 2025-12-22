# print 'CORRECT' if i == 10
v1 = int(input("Enter the value"))
if v1 == 10:
    print("Correct ",v1)
else:
     print("not Correct ",v1)
# Check the password, using if and else
password =input("Enter the password: ")
if password == "HOPE@123":
    print("Your password is correct")
else:
     print("Your password is Incorrect")

# Catagory the people by their age like children, adult, citizen, senior citizen..
age = int(input("Enter your age"))
if age <=16:
  print("Children")
elif age <=30:
    print("adult")
elif age <= 50:
    print("citizen")
elif age <=60:
    print("senior citizen.")


# Find whether given number is positive or negative
value =int(input("Enter input value:"))
if value > 0:
    print("Positive number")
elif value < 0:
    print("negative number")


# Check whether the given number is divisible by 5
num =int(input("Enter input value:"))
if num%5 == 0:
   print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")