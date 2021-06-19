h = open('c:/Users/P Rohit/Desktop/input.txt')
content = h.readlines()

a = 0

for line in content:

    for i in line:

        if i.isdigit() == True:
            a = i
            break

print("Number of the employees:", a)

l = [7980, 22349, 999, 2799, 229900, 11101, 9999, 2195, 9800, 4999]
l.sort()
# print(l)
min = 0
temp = a
d = 10 - int(a)
a = int(a) - 1
min = l[a] - l[0]
for i in range(0, d):
    c = l[a] - l[i]
    if (c < min):
        min = c
        f = i

    a += 1

# print(i)
g = ['MI Band', 'Sandwich Toaster', 'Cult Pass', 'Scale', 'Fitbit Plus', 'Microwave Oven', 'Alexa', 'Digital Camera',
     'IPods', 'Macbook Pro']
q = int(i) + int(temp)
for j in range(i, q):
    print(g[j - 1], ' : ', l[j - 1])
print('And the difference between the choosen goodie with highest price and the lowest price is ', min)
h.close()
