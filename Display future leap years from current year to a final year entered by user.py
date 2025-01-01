#Display future leap years from current year to a final year entered by user
year=int(input(" Enter the year to be cheked"))
if year%4==0:
    print( year,"Is a leap year")
elif year%4==1:
    print(year,"Is not a leap year, next leap year=",year+3)
elif year%4==2:
    print(year,"Is not a leap year, next leap year=",year+2)
elif year%4==3:
    print(year,"Is not a leap year, next leap year=",year+1)   
else:
    print("Error")    