# generators.py
# based on http://www.youtube.com/watch?v=bD05uGo_sVI

# without generator:
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)

# example 1: converting to generator:
print ('\n example 1:')

def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])

#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))

for num in my_nums:
    print(num)

# example 2: with generator:
print ('\n example 2:')

my_nums = (x*x for x in [1,2,3,4,5])

print(my_nums)
#print(list(my_nums))

for num in my_nums:
    print(num)
