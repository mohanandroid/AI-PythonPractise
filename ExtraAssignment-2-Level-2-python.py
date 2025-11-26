# print 0 to 20 by using range
for temp in range(0,20):
 print(temp)


 # print range 10 to 20
for newtemp in range(10,20):
   print(newtemp)


# Print number of items in the list by using 'len'
list=[10, 20, 14, 55, 43, 87, 76]
print("Number of item in the List", len(list))

text="Artificial Intelligence"
for ch in text:
 print(ch)

print(input("-Your Name-"))
print(input("-Your Age-"))
print(input("-Your Profile-"))

tup= (1," Welcome", 2, "Hope")
print(tup)


tup1=(1,2,3,4)
tup2= ("Python","C#", "Android")
print(tup1, tup2)

# print Odd Numbers in the list
tup3=(20,10,16,19,25,1,276,188)
for n in tup3:
    if n%2!=0:
        print(n, " is odd")


# print even Numbers in the list
tup3=(20,10,16,19,25,1,276,188)
for n in tup3:
    if n%2==0:
        print(n, " is even")