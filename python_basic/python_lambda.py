def identity(x):
     return x

print(identity(2))
# using lambda
print((lambda x:x) (1))
(lambda x, y: print(f"{x + y}"))(2,3)

#Lambda functions are frequently used with higher-order functions
#which take one or more functions as arguments or return one or more functions.
high_ord_func = lambda x, func: x + func(x)

#lamda exercise
# use map + lamda 
# (lambda x: print(x+2))(2)
numbers = [1, 2, 3, 4, 5]
# func = lambda x: print(x*2)
# func(2)
result = list (map((lambda x: (x+2)), numbers))
print(result)

numbers = [10, 15, 22, 33, 40, 55] #filter only even 
filtered = list (filter(lambda x:x%2==0, numbers ))
print(filtered)

pairs = [("apple", 3), ("banana", 1), ("cherry", 2)]
'''
recall
sort modify the list 
sorted return a new list 
'''
pairs.sort(key=lambda x:x[1], reverse=True)
print(pairs)

print()