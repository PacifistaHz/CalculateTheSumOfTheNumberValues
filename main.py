sum=0;
number=input("Enter a number: ")

if number.isnumeric()==False:
    print("Please enter a number")
else:
    for i in number:
        sum+=int(i);
    print(number +  " The sum of the number values " + str(sum))