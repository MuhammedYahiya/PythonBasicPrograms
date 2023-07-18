P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interset: "))
T = float(input("duration of time: "))

SI = float((P*R*T)/100)
print("Simple interset is: "+ str(SI)) # here concatinate a string to float is not possible so change the type of SI from float to str