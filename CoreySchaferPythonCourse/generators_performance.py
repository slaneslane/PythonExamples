# generators_performance.py
# based on http://www.youtube.com/watch?v=bD05uGo_sVI

import resource
import random
import time

names = ['Szymon', 'Malina', 'Anita', 'George', 'Michael']
majors = ['BioTech', 'Runner', 'Psycho', 'PM', 'Spy']

print('Memory (Before): {}Mb'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

#t1 = time.clock()
#people = people_list(1000000)
#t2 = time.clock()

# loosing performance when passing to the list!
#t1 = time.clock()
#people = list(people_generator(1000000))
#t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory (After): {}Mb'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
print('Took {} seconds'.format(t2-t1))
