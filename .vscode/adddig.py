num=98457
sum=0
while num>0:
    dig=num%10
    sum+=dig
    num=num//10
print("Sum of digits of the given number:",sum)