                           # TEMPERATURE CONVERSION PROGRAM

print("        ** INFORMATIONS **")
print("To enter a value in degrees Celcius :-\n Enter choice = 1")
print("To enter a value in degrees Farenheit :-\n Enter choice = 2")
print("To enter a value in Kelvin Scale :-\n Enter choice = 3")

i=0
while(i<=1):
    if i==0:
        ch=int(input("Enter your choice = "))
        if ch > 3:
            print("Invalid Choice :(\n Kindly select choice value as 1, 2 or 3!")
        if ch==1:
            temp=float(input("Enter value in degrees Celcius = "))
            f=round(((temp*(9/5))+32),2)
            k=round((temp+273.15),2)
            print("Temperature in Farenheit :-\n ",temp," deg C = ",f," deg F")
            print("Temperature in Kelvin Scales :-\n ",temp," deg C = ",k," K")
        elif ch==2:
            temp=float(input("Enter value in degrees Farenheit = "))
            c=round(((temp-32)*(5/9)),2)
            k=round(((temp-32)*(5/9)+273.15),2)
            print("Temperature in Celsius :-\n ",temp," deg F = ",c," deg C")
            print("Temperature in Kelvin Scales :-\n ",temp," deg F = ",k," K")
        elif ch==3:
            temp=float(input("Enter value in Kelvin Scales = "))
            c=round((temp-273.15),2)
            f=round(((temp-273.15)*(9/5)+32),2)
            print("Temperature in Celsius :-\n ",temp," K = ",c," deg C")
            print("Temperature in Farenheit :-\n ",temp," K = ",f," deg F")
    n=int(input("For further coversion press 0, else press 1 :- "))
    i=n
    if i==1:
        print("EXIT :)")
        break



                