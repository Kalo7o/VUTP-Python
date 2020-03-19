start_year = int(input("Enter an year to start: "))
count=0
leap_years=[]
        
while(count<20):
    if(start_year%4==0 or start_year%100==0):
        leap_years.append(start_year)
        count=count+1
    start_year=start_year+1

print(leap_years)