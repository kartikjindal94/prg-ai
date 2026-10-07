sen=input("Enter a sentance:")
vow=0
con=0
dig=0
space=0
spec_char=0
for ch in sen:
    if ch.isalpha():
        if ch.lower() in ('aeiou'):
            vow+=1
        else:
            con+=1
    elif ch.isdigit():
        dig+=1
    elif ch.isspace():
        space+=1
    else:
        spec_char+=1
print(f"Words:{space+1}\nVowels:{vow}\nConsoants:{con}\nDigits:{dig}\nSpaces:{space}\nSpecial Characters:{spec_char}")