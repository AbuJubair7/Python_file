user_input=int(input("Input a number : "))

def prime(num):
    count=0
    for i in range(2,num+1):
        if num%i==0:
            count++
   return count
if prime(user_input)==1:
    print("Prime number")
else:
    print("Not a prime number")
 
#Minimized LOC(Line of code)
