"""
TailorSonam_assign8_part2.py
Part 2: Sieve of Eratosthenes (Finding all Numbers within a range)

Written by: Sonam Tailor
Class Section: 003

Version: 3.6.2
Date: November 20, 2017
"""

#initialize the accumulator 
totalprimes=0
#ask the user for an n value
n=int(input("Enter a positive integer greater than or equal to 10: "))
#data validation
while n<10:
    print("The integer is not valid!")
    n=int(input("Enter a positive integer greater than or equal to 10: "))

#create a list where every number is prime 
numberlist=["P"]*(n+1)
#make sure the special cases 0 and 1 are not prime
numberlist[0]="N"
numberlist[1]="N"


for i in range(2,n+1):
    #check to see if multiples are beyond the end of our maximum range
    if i*2>n:
        break
    #if the value is prime then mark the multiples are not prime
    elif numberlist[i]=="P":
        for j in range(i*i,n+1,i):
            numberlist[j]="N"
    #if the value is not prime continue to the next number
    else:
        continue

#initialize the accumulator to make sure the max numbers on a line is 10
numbers_on_line=0
for num in range(n+1):
    #check to see if the value is prime
    if numberlist[num]=="P":
        #increase total prime accumulator 
        totalprimes+=1
        #check to see if the numbers on the line is 10
        if numbers_on_line%10!=0 or numbers_on_line==0:
            print(format(num,">4d"),end=" ")
        #move to a new line
        else:
            print("\n"+format(num,">4d"),end=" ")
        #increase accumulator 
        numbers_on_line+=1

#print total count of prime numbers
print("\nFound",totalprimes,"prime numbers!")


