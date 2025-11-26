print("Welcome to Assignment-1")

Num1 = 10
Num2 = 30
Add = int(Num1 + Num2)
print("Num1=",Num1)
print("Num2=",Num2)
print("Add=",Add)


#Body Mass Index
bmi = float(input("Enter BMI value: "))
if bmi<=18.5:
    print("Under weight")
elif 18.5 < bmi <=24.9:
    print("Normal weight")
elif 25 < bmi <=34:
    print("Overweight")
else:
    print("Obese")