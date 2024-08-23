#1.Decisions at the Crossroad
#Task1:Code correction
number= int(input("Enter a number"))

if number > 0:
    print('The number is positive.')
elif number == 0:
    print('The number is zero.')
else:
    print('The number is negative.')

#2.The Greatest Showdown
#Task1:Identify the Greatest
n1= int(input("Enter a number please?"))
n2= int(input("Enter another number?"))
n3= int(input("Enter a third number?"))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)  
else:
    print(n3)

#Task 2:Identify the Smallest
if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
else:
    print(n3)

#3.Leap Year Explorer
#Task 1: leap Year Checker
year = int(input("Enter a year"))

if (year%4==0 and year%100!=0) or year%400==0:
    print("Leap Year!") 
else:
    print("Not a leap year!")
