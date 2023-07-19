A = float(input("Enter the Amount: "))
P = float(input("Enter the pricipal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time span: "))

A =float( P*pow((1+R/100),T))
CI = float(A - P)
print("Compound Interest: " + str(CI))
