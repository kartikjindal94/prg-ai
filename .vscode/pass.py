password=input("Enter password:")
founduppercase=False
foundlowercase=False
founddigit=False
foundspecialcharacter=False
foundspace=False
for i in password:
    if i.isupper():
        founduppercase=True
    elif i.islower():
        foundlowercase=True
    elif i.isdigit(): 
        founddigit=True
    elif i.isspace():
        foundspace=True
    else:
        foundspecialcharacter=True
if founduppercase and foundlowercase and founddigit and len(password)>=8 and foundspecialcharacter and foundspace==False:
    print("Valid")
else:
    if not founduppercase:
        print("Invalid because it does'nt contain any uppercase")
    elif not foundlowercase:
        print("Invalid because it does'nt contain any lowercase")
    elif not founddigit:
        print("Invalid because it does'nt contain any digit")
    elif len(password)<8:
        print("Invalid because the password is too short")
    elif not  foundspecialcharacter:
        print("Invalid because it does'nt contain any special character")
    elif foundspace:
        print("Invalid because it contains space")