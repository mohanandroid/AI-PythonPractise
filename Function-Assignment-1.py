#list=[23,35,45,60]
def addition(a, b):
    addition= a+b
    return addition

print(addition(5,8))



# # Create a class and function, and list out the items in the list
def subFileds():
 print("Sub-fields in AI are:")
 list=["Machine Learning","Neural Networks","Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
 for item in list:
   print(item)

result= subFileds()
print(result)

#  # Create a function that checks whether the given number is Odd or Even
def oddEven():
  num= int(input("Enter input value"))
  if((num%2)!=1):
   return "Even number"
  else:
    return "odd numbber"
  
value= oddEven()
print(value)

# Create a function that tells elegibility of marriage for male and female according 
# to their age limit like 21 for male and 18 for female
def marriageElig():
  gender= input("Your Gender: ")
  age= int(input("Your age: "))
  if(age>21 and gender.upper()== 'MALE'):
    print("Your are Eligible")
  elif (age>18 and gender.upper()== 'FEMALE'):
     print("Your are Eligible")
  elif (age<21 and gender.upper()== 'MALE' or age<18 and gender.upper()== 'FEMALE'):
     print("Your are not Eligible")

elig= marriageElig()
print(elig)

class FindPercentage:
   def percentage():
    sub1 = int(input("Subject 1"))
    sub2 = int(input("Subject 2"))
    sub3 = int(input("Subject 3"))
    sub4 = int(input("Subject 4"))
    sub5 = int(input("Subject 5"))
    total= sub1+ sub2+ sub3+ sub4+ sub5
    percentage= total/500*100
    print("Percentage:",percentage)
FindPercentage.percentage()

class Triangle:
  def triangel():
   height= int(input("Enter the height: "))
   breadth= int(input("Enter the breadth: "))
   result= (height* breadth)/2
   print("Area of Triangle: ",result)
traing =Triangle.triangel()