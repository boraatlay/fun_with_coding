'''

Problem:

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''

fib_series = [1, 2]

while sum(fib_series[-2:]) < 4000000:
        fib_series.append(sum(fib_series[-2:]))

even_fibvals = []

for i in fib_series:
    if i % 2 == 0:
        even_fibvals.append(i)
   
print(sum(even_fibvals))
