
# coding: utf-8

# In[1]:


## The prime factors of 13195 are 5, 7, 13 and 29.What is the largest prime factor of the number 600851475143 ?

n, i = 600851475143, 1
while i < n:
    if n % i == 0:
        n = n // i
        i=1
    i += 1
print(n)
