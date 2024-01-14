total = 0

for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j


Counter = 0
while Counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        Counter += 2


print("Final total:", total)
