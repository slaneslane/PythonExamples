# list_comprehensions.py
# based on http://www.youtube.com/watch?v=3dt4OGnU5sM

#nums = [1,2,3,4,5,6,7,8,9,10]

## I want 'n' for each 'n' in nums
#my_list = []
#for n in nums:
#    my_list.append(n)
#print(my_list)

#my_list = [n for n in nums]
#print(my_list)




## I want 'n*n' for each 'n' in nums
#my_list = []
#for n in nums:
#    my_list.append(n*n)
#print(my_list)

#my_list = [n*n for n in nums]
#print(my_list)

#my_list = map(lambda n: n*n, nums)
#print(my_list)




## I want 'n' for each 'n' in nums if 'n' is even
#my_list = []
#for n in nums:
#    if n%2 == 0:
#        my_list.append(n)
#print(my_list)

#my_list = [n for n in nums if n%2 == 0]
#print(my_list)

## Using a filter + lambda
#my_list = filter(lambda n: n%2 == 0, nums)
#print(next(my_list)) # seems like filter is a generator now ! so this solution:
#for i in my_list:
#    print(i)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
#my_list = []
#for letter in 'abcd':
#    for num in range(4):
#        my_list.append((letter,num))
#print(my_list)

#my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
#print(my_list)






# Dictionary Comprehensions
names = ['Szymon', 'Malina', 'Anita', 'George', 'Michael']
majors = ['BioTech', 'Runner', 'Psycho', 'PM', 'Spy']
#print(zip(names, majors))  # seems like zip is a generator now ! so this solution:
#zipped = zip(names, majors)
#for i in zipped:
#    print(i)


# I want a dict{'name': 'major'} for each name, hero in zip(names, majors)
#my_dict = {}
#for name, major in zip(names, majors):
#    my_dict[name] = major
#print(my_dict)

#my_dict = {name: major for name, major in zip(names, majors)}
#print(my_dict)

# If name not equal to George
#my_dict = {name: major for name, major in zip(names, majors) if name != 'George'}
#print(my_dict)







# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
#my_set = set()
#for n in nums:
#    my_set.add(n)
#print(my_set)



#my_set = {n for n in nums}
#print(my_set)


# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums

nums = [1,2,3,4,5,6,7,8,9,10]

#def gen_func(nums):
#    for n in nums:
#        yield n*n

#my_gen = gen_func(nums)

#for i in my_gen:
#    print(i)



my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)

