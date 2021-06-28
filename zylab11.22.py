"Peter Nguyen"
"6/27/2021"
"CIS2348"
"1860823"
"11.22 CIS 2348 LAB: Word frequencies"

words = input().split()
for word in words:
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(word, count)