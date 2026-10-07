age=int(input("Enter your age:"))
if age>=18:
    print("You can vote")
else:
    print("You can't vote")
    print("wait for",18-age,"years to vote")