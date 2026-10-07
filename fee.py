t_fee=input=(int("Enter Tuition Fee:"))
e_fee=input=(int("Enter Exam Fee:"))
lib_fee=input=(int("Enter Library Fee:"))
disc=3000
sum = t_fee + e_fee + lib_fee
total_fee = sum - disc
annual_fee = total_fee * 2
monthly_fee = annual_fee/12
print(monthy_fee)