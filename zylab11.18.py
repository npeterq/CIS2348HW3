"Peter Nguyen"
"6/27/2021"
"CIS2348"
"1860823"
"11.18 CIS 2348LAB: Filter and sort a list"


integers = input().split()
non_neg_int=[]

for num in integers:
    num = int(num)
    if num >= 0:
        non_neg_int.append(num)

non_neg_int.sort()

for i in non_neg_int:
    print(i,end=' ')