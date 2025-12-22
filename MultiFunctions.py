class MultiFuctions:
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
    
    def oddEven():
        num= int(input("Enter input value"))
        if((num%2)!=1):
            print("Even number")
            return "Even number"
        else:
            print("odd number")
            return "odd numbber"
        
    def marriageElig():
        gender= input("Your Gender: ")
        age= int(input("Your age: "))
        if(age>21 and gender.upper()== 'MALE'):
            print("Your are Eligible")
        elif (age>18 and gender.upper()== 'FEMALE'):
            print("Your are Eligible")
        elif (age<21 and gender.upper()== 'MALE' or age<18 and gender.upper()== 'FEMALE'):
            print("Your are not Eligible")

    def percentage():
        sub1 = int(input("Subject 1"))
        sub2 = int(input("Subject 2"))
        sub3 = int(input("Subject 3"))
        sub4 = int(input("Subject 4"))
        sub5 = int(input("Subject 5"))
        total= sub1+ sub2+ sub3+ sub4+ sub5
        percentage= total/500*100
        print("Percentage:",percentage)

    def triangel():
        height= int(input("Enter the height: "))
        breadth= int(input("Enter the breadth: "))
        result= (height* breadth)/2
        print("Area of Triangle: ",result)