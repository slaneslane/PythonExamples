# pythonic.py
# based on: https://www.youtube.com/watch?v=x3v9zMX1s4s&t=1s

# Duck Typing and Easier to ask forgiveness then persmission (EAFP)

class Duck(object):

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap')

class Person(object):

    def quack(self):
        print('I am Quacking like a duck!')

    def fly(self):
        print('I am flapping my arms!')

#def quack_and_fly(thing):
#    # not Duck-Typed(non-Pythonic)
#    if isinstance(thing, Duck):
#        thing.quack()
#        thing.fly()
#    else:
#        print('This has to be a duck!')

#def quack_and_fly(thing):
#    # Duck-Typed(Pythonic)
#    thing.quack()
#    thing.fly()

#def quack_and_fly(thing):
#    # LBYL (non-Pythonic)
#    if hasattr(thing, 'quack'):
#        if callable(thing.quack):
#            thing.quack()
#
#    if hasattr(thing, 'fly'):
#        if callable(thing.fly):
#            thing.fly()

def quack_and_fly(thing):
    # LBYL (Pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark() # doesn't exists!
    except AttributeError as e:
        print(e)

    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
