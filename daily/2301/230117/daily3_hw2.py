year=int(input())

if year%4==0 and year%10 !=0 or year%400==0:
    print('윤년')
else:
    print('윤년이 아님')