num1 = int(input("Enter the no :"))
num2 = int(input("Enter the no :"))
for i in range (num1,num2+1):
    num1=i
    num2=0
    while(num1!=0):
        rem=num1%10
        num1=int(num1/10)
        num2=num2*10+rem
    if (i==num2):
         print (i,end="")
           