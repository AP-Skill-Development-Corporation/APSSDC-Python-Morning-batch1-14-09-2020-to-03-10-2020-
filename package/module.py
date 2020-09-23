def average(start,end):
    s = 0
    c = 0
    for i in range(start,end+1):
        s = s + i
        c = c + 1
    print("Average: ", s/c)
    
    
def leapyears(l,u):
    for year in range(l,u+1):
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            print(year,end=" ")
