a=[]
n=int(input('n? '))
for i in range (n):
    temp=[]
    for j in range(n):
        temp.append(int(input()))
    a.append(temp)
summ = 0    
for i in range(n):
    for j in range(n):
        if i==j:
            summ = summ +a[i][j]
print(a)            
print(summ)


import random

print(random.randint(1, 10))
print(random.choice([1, 3, 5, 8, 9]))
print(random.uniform(1, 10))
print(random.random())
