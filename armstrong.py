n = int(input("Enter the no :"))
sum = 0
            
while n > 0:
        d = n %10
        sum += d**3
        n=n//10
if (n==sum):
     print ("armstrong")
else :
   print ("not  armstrong")
        
              
              
              
              
              
              
