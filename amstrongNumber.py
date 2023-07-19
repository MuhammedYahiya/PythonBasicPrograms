num = int(input("Enter a number to find its a amstrong or not: "));
len = len(str(num))
temp  = num

sum = 0;
while num !=0:
    r = num% 10
    sum = sum+(r**len)
    num = num//10;

if temp == sum:
    print("The given number is armstrong number")
else:
    print("The given nummber is not armstrong")
    



