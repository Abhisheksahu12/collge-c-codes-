n = int(input("Enter the no :"))
sum = 0
rev=0            
while n > 0:
        d = n %10
        rev=rev*10+d
        n=n//10
if (n==rev):
     print ("palindrome")
else :
   print ("not  palindrome ")
        
              
              
              
              
              
              
