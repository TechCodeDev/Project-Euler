
# coding: utf-8

# In[1]:


## If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
## Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_x_and_y(x, y, limit):
    answer = 0
    for i in range(0, limit):
        if i % x == 0 or i % y == 0:
            answer = answer + i
    return answer


print(multiples_of_x_and_y(3, 5, 1000))

