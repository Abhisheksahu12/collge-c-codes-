n = int (input ("Enter the nos : "))
reverse_no=0
while (n!=0):
    d = n%10
    reverse_no=reverse_no*10+d
    n=n//10
    print ("Reverse no is : " + str (reverse_no))
