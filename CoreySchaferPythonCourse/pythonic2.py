# pythonic2.py
# based on: https://www.youtube.com/watch?v=x3v9zMX1s4s&t=1s

# Duck Typing and Easier to ask forgiveness then persmission (EAFP)

#person = {'name': 'Jess', 'age': 22, 'job': 'Programmer'}
person = {'name': 'Jess', 'age': 22}

# LBYL (non-Pythonic)
#if 'name' in person and 'age' in person and 'job' in person:
#    print("I'm {name}. I'm {age}. I'm a {job}.".format(**person))
#else:
#    print('Missing some keys!')

# LBYL (Pythonic)
#try:
#    print("I'm {name}. I'm {age}. I'm a {job}.".format(**person))
#except KeyError as e:
#    print('Missing {} key!'.format(e))


my_list = [1,2,3,4,5]
# non-Pythonic
#if len(my_list) > 6:
#    print(my_list[5])
#else:
#    print('That index does not exists!')

# Pythonic
try:
    print(my_list[5])
except IndexError:
    print('That index does not exists!')
