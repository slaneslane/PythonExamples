# fibonacci.py
# based on http://www.youtube.com/watch?v=DEwgZNC-KyE

#a, b = 0, 1
#for i in range(10):
#    print(a)
#    a, b = b, a + b

# Fibonacci Generator:
def fib(num):
    a, b = 0, 1
    for i in xrange(num):
        yield a
        a, b = b, a + b

for item in fib(10):
    print(item)
