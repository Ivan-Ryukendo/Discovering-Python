def oddsum():
    i = 1
    sum = 0
    for i in range(100):
        if i % 2 == 0:
            continue
        sum = sum + 1

    return sum
    
num = oddsum()
print(num)