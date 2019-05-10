## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.What is the smallest positive
## number that is evenly divisible by all of the numbers from 1 to 20?


p = 0
i = 20
while True:
    ns = []
    for j in range(2, 21):
        if i%j != 0:
            break
        else:
            ns.append(j)
    if len(ns) == 19:
        break
    i+=1
print(i)
