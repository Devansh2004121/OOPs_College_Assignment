#Program to check that the inputted no. is armstrong or not
x=int(input("Enter the no. you want to check:"))
orig=x

sum=0

while (x>0):
    sum=sum+(x%10)*(x%10)*(x%10)
    x=x//10
if orig==x:
    print("Yes is an armstrong no.")
else:
    print("No is not an armstrong no.")
