a = open('can i read.txt', 'w')
a.write("read is a thing?")
a.close
b = open('can i read.txt', 'r')
sum = b.read()
print(sum)
a.close