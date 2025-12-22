class SubFieldinAI:
    def subFileds():
       print("Sub-fields in AI are:")
       items = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
       for item in items:
        print(item)

SubFieldinAI.subFileds()


# Create a function that checks whether the given number is Odd or Even
class OddEven:
 def oddEven():
  num= int(input("Enter input value"))
  if((num%2)!=1):
   print("Even number")
   return "Even number"
  else:
    print("odd number")
    return "odd numbber"
OddEven.oddEven()


# Create a function that tells elegibility of marriage for male and female according 
# to their age limit like 21 for male and 18 for female
class ElegiblityForMarriage:
 def marriageElig():
  gender= input("Your Gender: ")
  age= int(input("Your age: "))
  if(age>21 and gender.upper()== 'MALE'):
    print("Your are Eligible")
  elif (age>18 and gender.upper()== 'FEMALE'):
     print("Your are Eligible")
  elif (age<21 and gender.upper()== 'MALE' or age<18 and gender.upper()== 'FEMALE'):
     print("Your are not Eligible")
ElegiblityForMarriage.marriageElig()

# calculate the percentage of your 10th mark
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

#print area and perimeter of triangle using class and func
class Triangle:
  def triangel():
   height= int(input("Enter the height: "))
   breadth= int(input("Enter the breadth: "))
   result= (height* breadth)/2
   print("Area of Triangle: ",result)
traing =Triangle.triangel()