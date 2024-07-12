def odd_numbers():
    for num in range(2, 100, 2):
        print(num)

odd_nums_generator = odd_numbers()
for num in odd_nums_generator:
    print(num)