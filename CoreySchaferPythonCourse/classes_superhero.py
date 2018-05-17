# classes_superhero.py
# based on http://www.youtube.com/watch?v=DEwgZNC-KyE

class Person(object):

    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print "My name is {}".format(self.name)

class SuperHero(Person):

    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print "... and I am {}".format(self.hero_name)

szymon = Person('Szymon')
szymon.reveal_identity()

clark = SuperHero('Clark', 'Superman')
clark.reveal_identity()
