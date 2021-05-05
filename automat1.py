print('HELLO')

class Person:
    titles = ('Mr', 'Mrs', 'Ms')

    def __init__(self, first_name, last_name, email='' ):
        self.first_name = first_name
        self.last_name = last_name
    

person = Person('Jan', 'Kowalski')
print(person.titles)

