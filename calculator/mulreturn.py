def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("leap year")
    else:
        print("Not leap year")

def days_in_month(year, month):
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]       


#code :

year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))
days = days_in_month(year, month)
print(days)